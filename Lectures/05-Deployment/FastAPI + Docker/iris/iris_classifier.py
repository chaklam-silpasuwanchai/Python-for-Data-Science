from ossaudiodev import SNDCTL_DSP_SPEED
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


class IrisClassifier():
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        self.clf = self.train_model()
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self) -> LogisticRegression:
        return LogisticRegression(solver='lbfgs', max_iter=1000,
                                  multi_class='multinomial').fit(self.X, self.y)

    def classify(self, features: dict):
        X = [features['sepal_l'], features['sepal_w'],
             features['petal_l'], features['petal_l']]  # need bracket to add extra dimension for sklearn
        prediction = self.clf.predict_proba([X])
        return {
            'class': self.iris_type[np.argmax(prediction)], # no need to specify axis because assume one sample
            'probability': round(max(prediction[0]), 2)     # [0] to come out of extra dimension
                }
    