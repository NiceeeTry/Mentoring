"""The entrypoint module."""
import pandas as pd
import src.titanic_tutorial.constants as c
import src.titanic_tutorial.operations as op
import src.titanic_tutorial.preprocess as pre
import typer


def run(input_path: str, test_path: str, result_path: str = c.RESULT_DATA_PATH) -> None:
    """Runs the process including data splitting, preprocessing, training, prediction, and saving
    predictions."""
    titanic_data = pd.read_csv(input_path)
    titanic_test_data = pd.read_csv(test_path)

    strat_train_set, strat_test_set = pre.data_splitting(titanic_data)

    X_data, Y_data = pre.data_preprocessing(strat_train_set)
    final_clf = op.train(X_data, Y_data)
    X_data_test, Y_data_test = pre.data_preprocessing(strat_test_set)

    print(f"Prediction score: {final_clf.score(X_data_test, Y_data_test)}")

    X_data_final, y_data_final = pre.data_preprocessing(titanic_data)
    prod_final_clf = op.train(X_data_final, y_data_final)
    X_data_final_test = pre.prediction_data_preprocessing(titanic_test_data)

    op.predict(prod_final_clf, X_data_final_test, titanic_test_data, result_path)


if __name__ == "__main__":
    typer.run(run)
