from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
class LogClassifier:
    def __init__(self):
        self.model=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2))),("clf",LogisticRegression(max_iter=1000))])
        self.ready=False
    def fit_demo(self):
        x=["DRC PASS","LVS PASS","simulation converged","fatal convergence error","LVS mismatch","DRC violation","license checkout failed","job killed"]
        y=["PASS","PASS","PASS","RETRY","FAIL","FAIL","RETRY","RETRY"]
        self.model.fit(x,y);self.ready=True
    def classify(self,text):
        if not self.ready:self.fit_demo()
        return self.model.predict([text])[0]
