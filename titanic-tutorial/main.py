"""The entrypoint module."""
import pandas as pd
import src.titanic.constants as c
import src.titanic.operations as op
import src.titanic.preprocess as pre


def run() -> None:
    """Runs the process including data splitting, preprocessing, training, prediction, and saving
    predictions."""
    titanic_data = pd.read_csv(c.TRAIN_DATA_PATH)
    titanic_test_data = pd.read_csv(c.TEST_DATA_PATH)

    strat_train_set, strat_test_set = pre.data_splitting(titanic_data)

    X_data, Y_data = pre.data_preprocessing(strat_train_set)
    final_clf = op.train(X_data, Y_data)
    X_data_test, Y_data_test = pre.data_preprocessing(strat_test_set)

    print(f"Prediction score: {final_clf.score(X_data_test, Y_data_test)}")

    X_data_final, y_data_final = pre.data_preprocessing(titanic_data)
    prod_final_clf = op.train(X_data_final, y_data_final)
    X_data_final_test = pre.prediction_data_preprocessing(titanic_test_data)

    op.predict(prod_final_clf, X_data_final_test, titanic_test_data)


if __name__ == "__main__":
    run()
