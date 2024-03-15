import pandas as pd
from scipy.stats import shapiro
from src.titanic_tutorial import preprocess as pre


def test_split_data(mock_data: pd.DataFrame):
    train_set, test_set = pre.split_data(mock_data)
    input_length = len(mock_data)
    test_length = len(test_set)
    assert isinstance(train_set, pd.DataFrame)
    assert isinstance(test_set, pd.DataFrame)
    assert not train_set.empty
    assert not test_set.empty
    assert 0.15 <= test_length / input_length <= 0.25


def test_preprocess_data(sample_data: pd.DataFrame):
    X, y = pre.preprocess_data(sample_data)
    res = shapiro(y)
    assert res.statistic > 0.5
    res = shapiro(X)
    assert res.statistic > 0.05
