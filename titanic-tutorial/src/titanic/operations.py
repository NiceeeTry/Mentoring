"""This module provides functions for model training and data prediction."""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import src.titanic.constants as c


def train(X_data: np.ndarray, Y_data: np.ndarray) -> RandomForestClassifier:
    """Trains a Random Forest classifier using grid search for hyperparameter tuning.

    Args:
        X_data (numpy.ndarray): Features.
        Y_data (numpy.ndarray): Labels.

    Returns:
        RandomForestClassifier: Trained classifier.
    """
    clf = RandomForestClassifier()
    param_grid = [
        {
            "n_estimators": [10, 100, 200, 500],
            "max_depth": [None, 5, 10],
            "min_samples_split": [2, 3, 4],
        }
    ]
    grid_search = GridSearchCV(clf, param_grid, cv=3, scoring="accuracy", return_train_score=True)
    grid_search.fit(X_data, Y_data)
    final_clf = grid_search.best_estimator_
    return final_clf


def predict(clf: RandomForestClassifier, data: np.ndarray, test_data: pd.DataFrame) -> None:
    """Creates predictions and saves them to a CSV file.

    Args:
        clf (RandomForestClassifier): Trained classifier.
        data (numpy.ndarray): Preprocecessed data.
        test_data (pandas.DataFrame): Original data to get passenger Ids
    """
    predictions = clf.predict(data)
    final_df = pd.DataFrame(test_data["PassengerId"])
    final_df["Survived"] = predictions
    final_df.to_csv(c.RESULT_DATA_PATH, index=False)
