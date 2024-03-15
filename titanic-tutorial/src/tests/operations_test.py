import os

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.titanic_tutorial import operations as op
from src.titanic_tutorial import preprocess as pre


def test_train(sample_data: pd.DataFrame):
    X, y = pre.preprocess_data(sample_data)
    clf = op.train(X, y)
    assert isinstance(clf, RandomForestClassifier)


def test_predict(sample_data: pd.DataFrame, sample_test: pd.DataFrame):
    X, y = pre.preprocess_data(sample_data)
    clf = op.train(X, y)

    result_path = "data/result.csv"
    test = pre.preprocess_prediction_data(sample_test)
    predictions = op.predict(clf, test, sample_test, result_path)
    assert len(predictions) > 0
    assert os.path.exists(result_path)

    os.remove(result_path)
