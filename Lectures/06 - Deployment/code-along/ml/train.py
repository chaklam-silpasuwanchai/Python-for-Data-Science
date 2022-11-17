from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump #many lib to do this.....

#import datasets
iris = datasets.load_iris(return_X_y=True)
X, y = iris

#set up the pipeline
#standardize first, then logistic regression
pipeline_dict = [('scaling', StandardScaler()), 
                ('clf', LogisticRegression())]

pipeline = Pipeline(pipeline_dict)

#fit
pipeline.fit(X, y) #no train or test, for the sake of simplicity

#save the model
dump(pipeline, 'iris.joblib')

#this is overly simple, but for the sake of simplicity......