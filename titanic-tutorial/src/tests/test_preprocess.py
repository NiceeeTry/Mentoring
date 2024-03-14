import numpy as np
import pandas as pd
import pytest
from titanic_tutorial import preprocess as pre


def test_data_splitting(sample_data):
    with pytest.raises(ValueError):
        train_set, test_set = pre.data_splitting(sample_data)
        assert isinstance(train_set, pd.DataFrame)
        assert isinstance(test_set, pd.DataFrame)


def test_data_preprocessing(sample_data):
    expected = np.array(
        [
            [
                -1.52752523,
                1.15470054,
                -0.54401632,
                -0.77459667,
                -0.53881591,
                -0.56478964,
                -0.77459667,
                0.77459667,
                -1,
                1,
            ],
            [
                -1.09108945,
                -1.15470054,
                0,
                1.29099445,
                -0.53881591,
                None,
                1.29099445,
                -1.29099445,
                1,
                -1,
            ],
            [
                -0.65465367,
                1.15470054,
                -1.90405712,
                1.29099445,
                2.33486893,
                -0.09413161,
                -0.77459667,
                0.77459667,
                1,
                -1,
            ],
            [
                -0.21821789,
                -1.15470054,
                0,
                -0.77459667,
                -0.53881591,
                -0.75305286,
                1.29099445,
                -1.29099445,
                1,
                -1,
            ],
            [
                0.21821789,
                0,
                0.81602448,
                -0.77459667,
                -0.53881591,
                0.37652643,
                -0.77459667,
                0.77459667,
                -1,
                1,
            ],
            [
                0.65465367,
                -1.15470054,
                1.83605508,
                1.29099445,
                0.89802651,
                2.25915858,
                1.29099445,
                -1.29099445,
                1,
                -1,
            ],
            [
                1.09108945,
                0,
                0,
                -0.77459667,
                -0.53881591,
                -0.84718447,
                -0.77459667,
                0.77459667,
                -1,
                1,
            ],
            [
                1.52752523,
                1.15470054,
                -0.20400612,
                -0.77459667,
                -0.53881591,
                -0.37652643,
                -0.77459667,
                0.77459667,
                -1,
                1,
            ],
        ]
    )
    X, y = pre.data_preprocessing(sample_data)
    X == expected
