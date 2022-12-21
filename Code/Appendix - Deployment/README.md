# Deploying machine learning model to production

Out there, it is very difficult to find one tutorial covering the whole process.  Thus, in this tutorial, you will be learning of making a full stack of machine learning applications consisting of the following tools.  But please be reminded that learning tools are not as important as learning the process and the philosophy behind.

- FastAPI
- Docker
- Heroku
- Github actions
- Prometheus
- Grafana
- AWS EC2

## Table of contents

- [Deploying machine learning model to production](#deploying-machine-learning-model-to-production)
  - [Table of contents](#table-of-contents)
  - [Part 1: Fast API + Docker](#part-1-fast-api--docker)
    - [Prerequisites](#prerequisites)
    - [API](#api)
    - [FastAPI](#fastapi)
    - [Let's get started](#lets-get-started)
    - [1. Create a new directory called `ml`.](#1-create-a-new-directory-called-ml)
    - [2. Train a simple classifier](#2-train-a-simple-classifier)
    - [3. Define a placeholder classifier](#3-define-a-placeholder-classifier)
    - [4. Define the schema](#4-define-the-schema)
    - [5. Define the router](#5-define-the-router)
    - [6. Try run the uvicorn server to see how the API is](#6-try-run-the-uvicorn-server-to-see-how-the-api-is)
    - [7. Include dependencies](#7-include-dependencies)
    - [8. Dockerfile](#8-dockerfile)
    - [9. Build and run the container](#9-build-and-run-the-container)
    - [10. Use the API](#10-use-the-api)
    - [Congrats!!](#congrats)
  - [Part 2: Heroku + Github Action](#part-2-heroku--github-action)
    - [1. Install heroku cli](#1-install-heroku-cli)
    - [2. Login](#2-login)
    - [3. Create heroku app](#3-create-heroku-app)
    - [4. Push and deploy](#4-push-and-deploy)
    - [5. Changing app](#5-changing-app)
    - [6. Continuous integration with Github action](#6-continuous-integration-with-github-action)
    - [Congrats!](#congrats-1)
  - [Part 3: Prometheus + Grafana](#part-3-prometheus--grafana)
    - [Pre-requisities](#pre-requisities)
    - [0. Make some folders](#0-make-some-folders)
    - [1. Expose endpoints for prometheus](#1-expose-endpoints-for-prometheus)
    - [2. Add `prometheus-fastapi-instrumentator` to your `requirement.txt`](#2-add-prometheus-fastapi-instrumentator-to-your-requirementtxt)
    - [3. Define the configuration - `prometheus.yml` under the directory `prometheus`](#3-define-the-configuration---prometheusyml-under-the-directory-prometheus)
    - [4. Define the docker compose file](#4-define-the-docker-compose-file)
    - [5. Check whether everything is running fine](#5-check-whether-everything-is-running-fine)
    - [6. Grafana](#6-grafana)
    - [7. Modify the docker compose file to include grafana](#7-modify-the-docker-compose-file-to-include-grafana)
  - [Part 4: Deploy to AWS EC2](#part-4-deploy-to-aws-ec2)
    - [1. Launch an instance](#1-launch-an-instance)
    - [2. Name and os](#2-name-and-os)
    - [3. Instance type and key pair](#3-instance-type-and-key-pair)
    - [4. Network setting](#4-network-setting)
    - [5. Launch the instance](#5-launch-the-instance)
    - [6. Check your instance](#6-check-your-instance)
    - [7. Check the server address](#7-check-the-server-address)
    - [8. Add incoming ports](#8-add-incoming-ports)
    - [9. Connect to the instance](#9-connect-to-the-instance)
    - [10. Update and install stuffs](#10-update-and-install-stuffs)
    - [11. Run your application](#11-run-your-application)
    - [Congrats!!  What's next?  AWS Lambda](#congrats--whats-next--aws-lambda)
    - [References](#references)

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
- Allows data validation(e.g., maximum length, type)
- Supports error messages

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


### 7. Include dependencies

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

## Part 2: Heroku + Github Action

Let's deploy our app online.  We gonna use **Heroku** which is free but also support paid version.

### 1. Install heroku cli 
(You can do it in any directory)

```shell
brew tap heroku/brew && brew install heroku
```

If you are using other os, please refer to 

https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

### 2. Login 

Login to your heroku

(You can do it in any directory)

```shell
heroku login
heroku container:login
```

### 3. Create heroku app

(You can do it in any directory; app name can be anything)

```shell
heroku create [app-name]
```

To check that you have really created the app, you can go to heroku website and check.

![app](figures/app.png)

### 4. Push and deploy

Before we do anything, we have to revise the port variable in `Dockerfile`.  This is because heroku has its own port.

You can check the PORT variable via

```shell
heroku run printenv -a [app-name]
```

Revise your `Dockerfile` to:

```dockerfile
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 5000 <--we don't need this

CMD uvicorn --host 0.0.0.0 --port $PORT app:app
```

Now, let's push to heroku container register.  Go to the level where the Dockerfile is:

```shell
heroku container:push web -a [app-name]
```

(Note:  The first time I did this, it freezes.  Not sure why, but once I restarted my mac, it works fine.)

Then let's release to the public

```shell
heroku container:release web -a [app-name]  
```

Now go to 

    http://[app-name].herokuapp.com/docs

If you want to change the domain name, just simply purchase a domain name and link with it.

(Note: if your app is not running, check the logs:  `heroku logs -a [app-name]`)

### 5. Changing app

Now let's try add something in the `app.py` and see whether the changes propagate

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Again, we just repeat the two steps:

```shell
heroku container:push web -a [app-name]
heroku container:release web -a [app-name]  
```

Go to 

    http://[app-name].herokuapp.com   

You will see the changes.

### 6. Continuous integration with Github action

Now, this process can be automated, which is called **continuous integration** or **CI/CD**.  The idea is that whenever we push the code, it must run certain steps for us, such as test and deploy procedure for us.  There are two popular CI/CD frameworks which are **Jenkin** and **Github action**.  Since **Github action** has received a lot of interest lately, we shall explore it.

First, create a directory `.github` on the root level (at the same level as the root level of the repository)  (Note that the name cannot change because github action looks for this folder)

```shell
mkdir .github
```

Then inside .github, create a directory called `workflows`

```shell
cd .github
mkdir workflows
```

Inside the workflows, create the `main.yml` file

```shell
cd workflows
touch main.yml
```

Inside this, we shall define our github action, i.e., everytime we commit and push new code, it should help us automatically deploy to heroku.  The code is:

```yml
name: Deploy

on: push

jobs:
  build:  # any name is ok for this line
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.12 # this is the action
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}} #must be set in github > settings > secrets
          heroku_app_name: "iris-ait" #must exist
          heroku_email: "chaklam072@gmail.com"
          justlogin: true
      - run: |
          heroku container:login
          heroku container:push web -a iris-ait  
          heroku container:release web -a iris-ait

     #please change iris-ait to your app name
```

Go to your github repository, go to `Settings > Secrets`, set `HEROKU_API_KEY`.

![secrets](figures/secrets.png)


For the api key, run `heroku authorizations:create` for production apps, use `heroku auth:token` for development (you can do this anywhere in the terminal).

![auth](figures/auth.png)


If you want to further tweak, see https://github.com/marketplace/actions/deploy-to-heroku

To see that it is working, we can try change some of our API code like this:

```python
@app.get("/")
async def root():
    return {"message": "We change something"}
```

Then you can push and commit as usual.

You can check whether your `main.yml` is working by going to your github > actions.

![actions](figures/actions.png)

Then try to go to `http://[app-name].herokuapp.com` to see the change.

### Congrats!

Now we don't have to worry about running tedious commands.  Everything we push, these commands will be run.  What you can do more is to incorporate test in the github action.

In the next lab, let's try explore some monitoring tools.

## Part 3: Prometheus + Grafana


### Pre-requisities

```shell
pip install prometheus-fastapi-instrumentator
```

### 0. Make some folders

Before anything, let's clean things.  Let's put everything related to the fastapi into a directory called `app`.  In addition, please create a directory named `prometheus` and another directory named `grafana`.

The structure looks like this:

    .github  #for github actions
    app
        ml
        +-- classifier.py
        +-- train.py
        +-- iris_v1.joblib
        schema
        +-- iris.py
        app.py
        Dockerfile
        requirements.txt
    prometheus
        +-- prometheus.yml #will create shortly
    grafana
        +-- datasource.yaml #will create shortly
        +-- config.monitoring #will create shortly
    docker-compose.yaml  #will create shortly

### 1. Expose endpoints for prometheus 

In `app.py`, add the endpoints as

```python
from prometheus_fastapi_instrumentator import Instrumentator #put this in the beginning

Instrumentator().instrument(app).expose(app)  #you can put this at the last line of the file
```

For more details how to use this instrumentator, read https://github.com/trallnag/prometheus-fastapi-instrumentator

### 2. Add `prometheus-fastapi-instrumentator` to your `requirement.txt`

Now, my `requirement.txt` looks like this:

    fastapi==0.78.0
    numpy==1.23.1
    scikit_learn==0.24.2
    starlette==0.19.1
    uvicorn==0.18.2
    joblib==0.17.0
    pydantic==1.9.1
    prometheus-fastapi-instrumentator

### 3. Define the configuration - `prometheus.yml` under the directory `prometheus`

```yml
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).
# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"
# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.
    static_configs:
    - targets: ['localhost:9090']
  - job_name: 'app'
    dns_sd_configs: #automatic service discovery
      - names: ["app"]
        port: 8000
        type: A  #<--DNS A Record
        refresh_interval: 5s
```

For more details:  read https://prometheus.io/docs/prometheus/latest/configuration/configuration/



### 4. Define the docker compose file

Since we now have many services, it is good practice to run all of them together in a docker-compose file.  

Before we create the `docker-compose.yaml` file, let's remove the port number from the `Dockerfile`:

```dockerfile
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn --host 0.0.0.0 app:app
```

Now create a `docker-compose.yaml` as follows:

```yaml
version: "3.8"

services:
  app:
    build: .  #<---simply build the current directory Dockerfile
    restart: unless-stopped
    container_name: app
    ports:
      - 8000:8000
    networks:
      example-network:
        ipv4_address: 172.16.238.10

  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    container_name: prometheus
    ports:
      - 9090:9090
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
    networks:
      example-network:
        ipv4_address: 172.16.238.11

networks: #a common network where all the service resides
  example-network:
    name: example-network
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.16.238.0/24
```

Now that we set up the endpoints and the yml file, let's run the compose file (you don't have to run the Dockerfile first):

```shell
docker compose up
```

### 5. Check whether everything is running fine

Fast API: Go to http://localhost:8000/docs

Prometheus:  Go to http://localhost:9090

Try put this in the execution box of prometheus:

`http_requests_total`  which will list the total number of requests.

If you want to try other metrics or add custom metrics, see https://github.com/trallnag/prometheus-fastapi-instrumentator

We can shut down all services again:

```shell
docker compose down
```

### 6. Grafana

As you can see, prometheus is not really a good visualizer.  It's more like a metric gatherer.  Grafana is commonly used together with Prometheus.

To set grafana, we have to create two files: the `datasource.yaml` specifying where is the datasource for grafana to visualize, and `config.monitoring` which specifies very basic configurations for grafana like password.

Let's start with the `datasource.yml` under the directory `grafana`.

```yml

# config file version
apiVersion: 1

# list of datasources to insert/update depending
# on what's available in the database
datasources:
  # <string, required> name of the datasource. Required
- name: Prometheus
  # <string, required> datasource type. Required
  type: prometheus
  # <string, required> access mode. direct or proxy. Required
  access: proxy
  # <string> url
  url: http://prometheus:9090

```

Create a `config.monitoring` file inside the grafana directory:

    GF_SECURITY_ADMIN_PASSWORD=pass@123
    GF_USERS_ALLOW_SIGN_UP=false

### 7. Modify the docker compose file to include grafana

```yaml
version: "3.8"

services:
  app:
    build: ./app  #<---simply build the current directory Dockerfile
    restart: unless-stopped
    container_name: app
    ports:
      - 8000:8000
    networks:
      example-network:
        ipv4_address: 172.16.238.10

  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    container_name: prometheus
    ports:
      - 9090:9090
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
    networks:
      example-network:
        ipv4_address: 172.16.238.11

  grafana:
    image: grafana/grafana:latest
    restart: unless-stopped
    user: "472"  #<--default user ID of grafana
    container_name: grafana
    depends_on:
      - prometheus
    ports:
      - 3000:3000
    volumes:
      - ./grafana/datasource.yaml:/etc/grafana/provisioning/datasources/datasource.yaml
    env_file:
      - ./grafana/config.monitoring
    networks:
      example-network:
        ipv4_address: 172.16.238.12

networks:
  example-network:
    name: example-network
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.16.238.0/24
```

Run

```shell
docker compose up
```

Now, go to http://localhost:3000

username is `admin` and password is `pass@123` as you specified in `config.monitoring`.

Now you can try Explore or Add Dashboard to suit your needs.

What is cool here is that even you restart your docker, all dashboards will still be persisted.

Read more here:  https://grafana.com/tutorials/grafana-fundamentals/?utm_source=grafana_gettingstarted

Next part, we shall deploy to AWS EC2.

## Part 4: Deploy to AWS EC2

Bad news....Heroku does not really support Prometheus nor Grafana out of the box.   It can be done but requires way too much of effort.  Thus we gonna try something easier, i.e., AWS EC2.

First, sign up AWS services.  Here you would require a credit card.  If you don't have one, don't worry, you can just read the tutorial and do it later.

There are three ways to do this: (1) through **docker context** but this way it forces us to use Fargate which is not free, (2) through **ecs-cli** but it is quite restrictive on the versions that docker compose supports, and (3) through **ec2** which is as simple as spawning a server.   We will be going to the EC2 route.

### 1. Launch an instance
Go to EC2 service.  Select the orange button to create a instance.  An instance is basically a server.

<img width=600 src ="figures/1-launch.png">

### 2. Name and os

- **Name**: set any name
- **OS Images**:  choose Ubuntu
  
<img width=600 src ="figures/2-name-os.png">

### 3. Instance type and key pair

- **Instance type**: Choose *t2.micro*; it's free for 1 year (but don't forget to turn this off, or you will be charged after a year!)
- **Key pair**: Create a new key-pair;  this will be used to ssh to the instance.   Any name is fine.

<img width=600 src ="figures/3-key.png">

### 4. Network setting

Tick all ssh, http, and https so our instance can be accessed from all three ways.

<img width=600 src ="figures/4-network.png">

### 5. Launch the instance

Once done, select Launch Instance (the orange button on the bottom right).

<img width=600 src ="figures/5-launch.png">

### 6. Check your instance

Go back to the home menu of instance, and you should see your instance initializing.  For now, please wait until it is ready.

<img width=600 src ="figures/6-check.png">

### 7. Check the server address

Click on the instance ID (blue link) and will direct you to metadata of the server.   Try look around.  Take note of the server address. 

<img width=600 src = "figures/7-summary.png">

### 8. Add incoming ports

Scroll down and select the Security tab

<img width=600 src = "figures/8-security.png">

Select the blue link on the Security groups.  You will be directed to tabs on inbound ruels:

<img width=600 src = "figures/9-incoming.png">

Click Edit Inbound rules and add in two ports for prometheus and grafana, and save.  Note that we are not going to specify 8000, since we will be using port 80 for fastapi.

<img width=600 src = "figures/10-ports.png">


### 9. Connect to the instance

Let's connect to the instance.  To get some guidelines how to do so, click "Connect" on the top right corner. 

<img width=600 src = "figures/11-connect.png" /><br/><br/>

Select ssh client, which will tell us how to actually connect to this instance via ssh.  If you are using mac/linux, it's perfect.

<img width=600 src = "figures/12-connect-ssh.png"><br/><br/>

Based on the instruction, let's open a terminal.  Copy the `fastapi_key.pem` to any place where you wanna ssh into (it does not really matter where; for mine is simply Desktop.)

At the same place where `fastapi_key.pem` resides, do

```shell
chmod 400 fastapi_key.pem
```

Connect to the instance (please use the address as your instance):

```shell
ssh -i "fastapi_key.pem" ubuntu@ec2-54-82-237-124.compute-1.amazonaws.com
```

Type "yes" (if this is your first time)

You will now be inside the ubuntu instance.  Yay!

<img width=600 src = "figures/13-ubuntu.png"><br/><br/>

### 10. Update and install stuffs

Let's treat this like a fresh ubuntu and start updating and installing the required stuffs.

```shell
#update our repository so we get access to all latest softwares
sudo apt-get update
```

Follow this https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04 and install the Docker and Docker Compose into the Ubuntu:

```shell
#install a few prerequisite packages which let apt use packages over HTTPS:
sudo apt -y install apt-transport-https ca-certificates curl software-properties-common

#adding the key to the official docker repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

#add the repo to apt
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#update again
sudo apt update

#Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
apt-cache policy docker-ce

#install docker
sudo apt install -y docker-ce docker-compose-plugin
```

### 11. Run your application

Clone your git repository:

```shell
git clone https://github.com/chaklam-silpasuwanchai/Deploy-ML-Production.git
```

Edit the `docker-compose.yaml` file and change the ports of Fastapi from 8000 to 80 like this:

<img width=600 src = "figures/14-api_port.png"><br/><br/>

Now run

```shell
sudo docker compose up
```

Recall your address of your AWS instance.  Go to that address, and you will see that everything is running (make sure you use http not https, as we are using port 80):

<img width=600 src = "figures/15-running.png"><br/><br/>

### Congrats!!  What's next?  AWS Lambda

Try reconfigure so that everytime we commit, it changes  for us :-).  

For your reference, look at the new `.github/workflows/main.yml` for some hints how to do so.

Another thing you may want to do is to instead deploy to **AWS Lambda** which offers function as a service.  This would dramatically reduce our cost, since the service is only short-lived.

Good luck exploring!

### References

- https://github.com/Kludex/fastapi-prometheus-grafana

- https://github.com/trallnag/prometheus-fastapi-instrumentator
