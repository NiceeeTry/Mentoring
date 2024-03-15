import pandas as pd
import pytest


@pytest.fixture
def sample_data() -> pd.DataFrame:
    titanic_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 3, 4, 5, 6, 7, 8],
            "Survived": [0, 1, 1, 1, 0, 1, 0, 0],
            "Pclass": [3, 1, 3, 1, 2, 1, 2, 3],
            "Name": [
                "Wilson, Mr. Thomas",
                "Baker, Mrs. Alice",
                "Clark, Miss. Sarah",
                "Evans, Mrs. Emily",
                "Martinez, Mr. Michael",
                "King, Mrs. Jennifer",
                "Garcia, Mr. William",
                "Phillips, Mr. Robert",
            ],
            "Sex": ["male", "female", "female", "female", "male", "female", "male", "male"],
            "Age": [28.0, None, 24.0, None, 32.0, 35.0, None, 29.0],
            "SibSp": [0, 1, 1, 0, 0, 1, 0, 0],
            "Parch": [0, 0, 2, 0, 0, 1, 0, 0],
            "Ticket": [
                "123456",
                "234567",
                "345678",
                "456789",
                "567890",
                "678901",
                "789012",
                "890123",
            ],
            "Fare": [10.0, 13, 15.0, 8.0, 20.0, 40.0, 7.0, 12.0],
            "Cabin": [None, None, None, None, None, None, None, None],
            "Embarked": ["S", "C", "S", "C", "S", "C", "S", "S"],
        }
    )
    return titanic_df


@pytest.fixture
def sample_test() -> pd.DataFrame:
    test_data = pd.DataFrame(
        {
            "PassengerId": [9, 10, 11, 12],
            "Pclass": [2, 1, 3, 2],
            "Name": ["Andrew Tate", "Selena White", "Clark Kent", "John Silver"],
            "Sex": ["male", "female", "female", "male"],
            "Age": [30, 21, 24.0, None],
            "SibSp": [0, 1, 1, 0],
            "Parch": [0, 1, 0, 0],
            "Ticket": ["343965", "102845", "195395", "123424"],
            "Fare": [13.0, 45, 5, 8.0],
            "Cabin": [None, None, None, None],
            "Embarked": ["S", "C", "S", "C"],
        }
    )
    return test_data


@pytest.fixture
def mock_data() -> pd.DataFrame:
    data = pd.read_csv("data/train.csv")
    return data
