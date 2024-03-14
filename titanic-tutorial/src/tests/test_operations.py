import os

from sklearn.ensemble import RandomForestClassifier
from titanic_tutorial import operations as op
from titanic_tutorial import preprocess as pre


def test_train(sample_data):
    X, y = pre.data_preprocessing(sample_data)
    clf = op.train(X, y)
    assert isinstance(clf, RandomForestClassifier)


def test_predict(sample_data, sample_test):
    X, y = pre.data_preprocessing(sample_data)
    clf = op.train(X, y)

    result_path = "../../data/result.csv"
    test = pre.prediction_data_preprocessing(sample_test)
    op.predict(clf, test, sample_test, result_path)
    assert os.path.exists(result_path)

    os.remove(result_path)
