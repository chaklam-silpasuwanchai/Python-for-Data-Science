## Part 2: Heroku + Github Action

Let's deploy our app online.  We gonna use **Heroku** which is free but also support paid version.

### Pre-requisites

Make sure you have a completely separate repository holding the app that we did last time.

Here is the separate repository of mine:

https://github.com/chaklam-silpasuwanchai/Deploy-ML-Production

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