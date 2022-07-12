# for serving endpoints
from fastapi import APIRouter

#for accepting JSON
from starlette.responses import JSONResponse

#import the class
from iris.iris_classifier import IrisClassifier

router = APIRouter()

@router.post('/classify')  #user send post request to this url
def classify_iris(features: dict):
    clf = IrisClassifier()
    return JSONResponse(clf.classify(features))  #the API return response as JSON




