"""This module provides utility functions for data preprocessing."""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class AgeImputer(BaseEstimator, TransformerMixin):
    """Transformer for imputing missing values in the 'Age' column.

    Methods:
        fit: Fits the transformer.
        transform: Transforms the data by imputing missing 'Age' values.
    """

    def fit(self, X: pd.DataFrame, y=None) -> BaseEstimator:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X


class FeatureEncoder(BaseEstimator, TransformerMixin):
    """Transformer for encoding categorical features.

    Methods:
        fit: Fits the transformer.
        transform: Transforms the data by encoding categorical features.
    """

    def fit(self, X: pd.DataFrame, y=None) -> BaseEstimator:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()

        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]

        matrix = encoder.fit_transform(X[["Sex"]]).toarray()
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X


class FeatureDropper(BaseEstimator, TransformerMixin):
    """Transformer for dropping unnecessary features.

    Methods:
        fit: Fits the transformer.
        transform: Transforms the data by dropping specified features.
    """

    def fit(self, X: pd.DataFrame, y=None) -> BaseEstimator:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.drop(["Embarked", "Name", "Ticket", "Cabin", "Sex", "N"], axis=1, errors="ignore")


pipline = Pipeline(
    [
        ("ageimputer", AgeImputer()),
        ("featureencoder", FeatureEncoder()),
        ("featuredropper", FeatureDropper()),
    ]
)


def split_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Splits the data into training and testing sets.

    Returns:
        tuple: Training and testing sets.
    """

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
    for train_indices, test_indices in split.split(data, data[["Survived", "Pclass", "Sex"]]):
        strat_train_set = data.loc[train_indices]
        strat_test_set = data.loc[test_indices]
    return strat_train_set, strat_test_set


def preprocess_data(strat_train_set: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Preprocesses the training data.

    Returns:
        tuple: Processed features and labels.
    """

    strat_train_set = pipline.fit_transform(strat_train_set)
    X_data, Y_data = prepare_training_data(strat_train_set)
    return X_data, Y_data


def prepare_training_data(training_set: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Prepares training data by scaling features and separating labels.

    Returns:
        tuple: Scaled features and labels.
    """

    X = training_set.drop(["Survived"], axis=1)
    Y = training_set["Survived"]
    scaler = StandardScaler()
    X_data = scaler.fit_transform(X)
    Y_data = Y.to_numpy()
    return X_data, Y_data


def preprocess_prediction_data(data: pd.DataFrame) -> np.ndarray:
    """Preprocesses test data for prediction.

    Returns:
        numpy.ndarray: Processed test data.
    """
    X_final_test = pipline.fit_transform(data)
    X_final_test = X_final_test.fillna(method="ffill")
    scaler = StandardScaler()
    X_data_final_test = scaler.fit_transform(X_final_test)
    return X_data_final_test
