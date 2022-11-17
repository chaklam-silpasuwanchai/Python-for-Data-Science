#the main file containing the FastAPI

#these are the files we just made
import ml.classifier as clf
from schema.iris import Iris

#these are other libs
from joblib import load
from fastapi import FastAPI

#1. define the fastapi instance
app = FastAPI()

#2. define the startup event
#format: to define the trigger, we use @ (similar to SpringBoot)
@app.on_event('startup') #whenever the app got started - uvicorn ...--port 5000
def load_model():
    clf.model = load('ml/iris.joblib')

#3. define the url for prediction
@app.post('/pred')
def predict(iris:Iris):  #expect a Iris data (is a list)
    data = dict(iris)['data']
    predictions = clf.model.predict(data).tolist()
    prob = clf.model.predict_proba(data).tolist()
    return {"prediction": predictions,
            "probability": prob}
    
