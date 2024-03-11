import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


TRAIN_DATA_PATH = "../data/train.csv"
TEST_DATA_PATH = "../data/test.csv"
RESULT_DATA_PATH = "../data/predictions.csv"


class Titanic:
    def __init__(self) -> None:
        self.titanic_data = pd.read_csv(TRAIN_DATA_PATH)
        self.titanic_test_data = pd.read_csv(TEST_DATA_PATH)
        self.pipline = Pipeline(
            [
                ("ageimputer", AgeImputer()),
                ("featureencoder", FeatureEncoder()),
                ("featuredropper", FeatureDropper()),
            ]
        )

    def run(self) -> None:
        strat_train_set, strat_test_set = self.data_splitting(self.titanic_data)

        X_data, Y_data = self.data_preprocessing(strat_train_set)
        final_clf = self.trainig(X_data, Y_data)
        X_data_test, Y_data_test = self.data_preprocessing(strat_test_set)

        print(f"Prediction score: {final_clf.score(X_data_test, Y_data_test)}")

        X_data_final, y_data_final = self.data_preprocessing(self.titanic_data)
        prod_final_clf = self.trainig(X_data_final, y_data_final)

        X_data_final_test = self.prediction_data_preprocessing()
        predictions = prod_final_clf.predict(X_data_final_test)
        self.create_predictions(predictions)

    def data_splitting(self, data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
        for train_indices, test_indices in split.split(data, data[["Survived", "Pclass", "Sex"]]):
            strat_train_set = data.loc[train_indices]
            strat_test_set = data.loc[test_indices]
        return strat_train_set, strat_test_set

    def data_preprocessing(
        self, strat_train_set: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        strat_train_set = self.pipline.fit_transform(strat_train_set)
        X_data, Y_data = self.training_data_preparation(strat_train_set)
        return X_data, Y_data

    def training_data_preparation(
        self, training_set: pd.DataFrame
    ) -> tuple[np.ndarray, np.ndarray]:
        X = training_set.drop(["Survived"], axis=1)
        Y = training_set["Survived"]
        scaler = StandardScaler()
        X_data = scaler.fit_transform(X)
        Y_data = Y.to_numpy()
        return X_data, Y_data

    def trainig(self, X_data: np.ndarray, Y_data: np.ndarray) -> RandomForestClassifier:
        clf = RandomForestClassifier()
        param_grid = [
            {
                "n_estimators": [10, 100, 200, 500],
                "max_depth": [None, 5, 10],
                "min_samples_split": [2, 3, 4],
            }
        ]
        grid_search = GridSearchCV(
            clf, param_grid, cv=3, scoring="accuracy", return_train_score=True
        )
        grid_search.fit(X_data, Y_data)
        final_clf = grid_search.best_estimator_
        return final_clf

    def prediction_data_preprocessing(self) -> np.ndarray:
        X_final_test = self.pipline.fit_transform(self.titanic_test_data)
        X_final_test = X_final_test.fillna(method="ffill")
        scaler = StandardScaler()
        X_data_final_test = scaler.fit_transform(X_final_test)
        return X_data_final_test

    def create_predictions(self, predictions: np.ndarray) -> None:
        final_df = pd.DataFrame(self.titanic_test_data["PassengerId"])
        final_df["Survived"] = predictions
        final_df.to_csv(RESULT_DATA_PATH, index=False)
        # print(final_df)


class AgeImputer(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame, y=None) -> BaseEstimator:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X


class FeatureEncoder(BaseEstimator, TransformerMixin):
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
    def fit(self, X: pd.DataFrame, y=None) -> BaseEstimator:
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.drop(["Embarked", "Name", "Ticket", "Cabin", "Sex", "N"], axis=1, errors="ignore")


if __name__ == "__main__":
    titantic = Titanic()
    titantic.run()

