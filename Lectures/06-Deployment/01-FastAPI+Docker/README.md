# Deploying machine learning model to production

Out there, it is very difficult to find one tutorial covering the whole process.  Thus, in this tutorial, you will be learning of making a full stack of machine learning applications consisting of the following tools.  But please be reminded that learning tools are not as important as learning the process and the philosophy behind.

- FastAPI
- Docker
- Heroku
- Github actions
- Prometheus
- Grafana
- AWS EC2

## Part 1: Fast API + Docker

Once we developed our ML model, we have to make it accessible by the public or at least the applications that require the prediction results.

To do that, we need to create an API in which the outside can easily access.  Particularly, what we want to achieve is:

>Our **ML model**  --access via--> **API** (e.g., FastAPI)  --access by--> **consumers** (e.g., websites, mobile, dashboard, IoT devices, etc).

This process of making your model accessible is called **deployment into production**.

So let's get started.

### Prerequisites

- Install Docker Desktop for Mac/Windows or Docker CLI for Linux
  - Supports latest `docker compose` not `docker-compose`
- Install FastAPI (pip install fastapi)
- Install uvicorn (pip install uvicorn)

### API

You build an API that acts as an entry point to your app, through HTTP requests such as GET, POST, PUT, DELETE.

### FastAPI

FastAPI is the most popular go-to framework for building robust and high-performance APIs that scale in production environments.

- Simple and easy to use
- Does not come with a webserver; commonly use **uvicorn** which is a lightning-fast ASGI server.
- FastAPI + uvicorn is one of the fastest
- Unlike Django or Flask, it supports asynchronous requests
- Does not come with a view component;  often used together with React/Vue/Angular/HTML for frontend
- Allows data validation (e.g., maximum length, type)
- Supports error messages
- Default UI like Postman

In this example, we will only be using two HTTP methods:

- <code>GET</code>: used to retrieve data from the application
- <code>POST</code>: used to send data to the application (required for inference)

### Let's get started

The directory structure is as follows:

    ml
    +-- classifier.py
    +-- train.py
    +-- iris_v1.joblib
    schema
    +-- iris.py
    app.py
    Dockerfile
    requirements.txt

### 1. Create a new directory called `ml`. 

This directory will contain all the code related to machine learning.

### 2. Train a simple classifier

For simplicity, let’s use Logistic Regression as our algorithm.

Create a `train.py` in your <code>ml</code> directory.  Put this code below:

```python
from joblib import dump
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# import dataset
iris = datasets.load_iris(return_X_y=True)
X = iris[0]
y = iris[1]

# train
pipeline_dict = [('scaling', StandardScaler()),
            ('clf', LogisticRegression())]

pipeline = Pipeline(pipeline_dict)

pipeline.fit(X, y)

# save model for deployment
dump(pipeline, 'iris_v1.joblib')
```


Note that this model is very simple...e.g., no scaling/splitting/gridsearch.  This is intended so we can quickly jump to deployment...

### 3. Define a placeholder classifier

Let's create a placeholder variable to hold the model, when we load, so we can reuse.

Create a `classifier.py` under the `ml` folder with the following code:

```python
clf = None
```

### 4. Define the schema

FastAPI has an automatic data validation, if we provide it with the `BaseModel` definition.

Create a directory `schema`, and create `iris.py` inside with the following code.

```python
from pydantic import BaseModel, conlist
from typing import List

# Without this file won't break your app, but it's good practice

#basically create a schema describing Iris
#mainly for the purpose of automatic data validation
class Iris(BaseModel):    
    #conlist helps imposing list with constraints
    data: List[conlist(float, 
                    min_items=4,
                    max_items=4)]
```

### 5. Define the router

Here we gonna define how url is routed.  You can see this as the *main()* file.

Create `app.py` in the root level.  In this script, we define the app and specify the router(s).

```python
#our classifier
import ml.classifier as clf
from fastapi import FastAPI, Body
from joblib import load

#Iris data structure
from schema.iris import Iris

#define the fastapi
app = FastAPI(title="Iris Prediction API",
            description="API for Iris Prediction",
            version="1.0")

#when the app start, load the model
@app.on_event('startup')
async def load_model():
    clf.model = load('ml/iris_v1.joblib')
    
#when post event happens to /predict
@app.post('/predict')
async def get_prediction(iris:Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    proba = clf.model.predict_proba(data).tolist() 
    return  {"prediction": prediction,
            "probability": proba}
```

### 6. Try run the uvicorn server to see how the API is

We are actually done with the API.  Yes!  It's that simple.

Run the server by:

```shell
uvicorn app:app --port 5000
```

Go to `http://127.0.0.1:5000/docs`.  Then try input some values and see the response by clicking **Try it out**.

You can also try only three values, and see the errors.

![swagger UI](figures/swagger.png)


### 7. Include Dependencies

Let's prepare ourselve containerize our app.  But before that, let's create a file containing all our dependencies.

At root, create a `requirements.txt` file to specify all of the dependencies required to build this app.

My requirements.txt looks like this:

    fastapi==0.78.0
    numpy==1.23.1
    scikit_learn==0.24.2
    starlette==0.19.1
    uvicorn==0.18.2
    joblib==0.17.0
    pydantic==1.9.1

If you don't know which version you are using, try `pip list`.

### 8. Dockerfile

We also need to create a Dockerfile which will contain the commands required to assemble the image. Once deployed, other applications will be able to consume from our iris classifier to make cool inferences about flowers.

```dockerfile
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000 

CMD uvicorn --host 0.0.0.0 --port 5000 app:app
```

The first line defines the Docker base image for our application. The `python:3.8-slim-buster` is a popular image — it’s lightweight and very quick to build. 

Our Dockerfile concludes with a `CMD` which is used to set the default command to `uvicorn --host 0.0.0.0 --port 5000 app:app`. The default command is executed when we run the container.

If you don't understand very well, don't worry!  There are many online materials how to make Dockerfile. :-)

### 9. Build and run the container

We are almost there!!

Build the docker image using 

```shell
docker build . -t iris
```

This step takes a while to finish.

Check whether you have successfully build the image

```shell
docker images
```

*Note: If you make any mistake, simply* `docker rmi [image_id]`*, and do the build again*.

After the image is built, generate the docker container using 

```shell
docker run --name iris -p 8000:5000 iris
```

Check whether your image is running

```shell
docker ps -a
```

*Note: If you want to stop, do* `docker stop [image_id]`*; if you want to remove the container, do* `docker rm [image_id]`*.  Do these until you are satisfied :-)*

This exposes the application to the port 8000. Running the container also kicks off the default command we set earlier — which effectively starts up the app!

### 10. Use the API

So let's try our API.

Go to `localhost:8000/docs`.  Now you can do the same thing.

Note: if you are using docker machine, replace localhost with the IP address you found in `docker machine ip`

### Congrats!!

In the next lab, let's deploy to **Heroku**, so everyone in the world can use your API.  Also let's try setup **CI/CD with github actions**.

#### References

- https://towardsdatascience.com/deploying-iris-classifications-with-fastapi-and-docker-7c9b83fdec3a
- https://medium.com/analytics-vidhya/serve-a-machine-learning-model-using-sklearn-fastapi-and-docker-85aabf96729b
