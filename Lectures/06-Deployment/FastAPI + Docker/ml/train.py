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

