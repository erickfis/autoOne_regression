"""
# Project AutoOne_regression

Auxiliary functions for cleanning data and building regression models

- Erick Medeiros Anastácio
- 2020-06-28
- Python 3.7

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
import sklearn.metrics as metrics
import time


def clean_data(df):
    """Cleans the incoming data.

    Args:
        df (pands df): Incoming dat

    Returns:
        df: Clean data.

    """
    df = df.copy()
    df = df.replace(to_replace='?', value=np.NaN)
    df.columns = df.columns.str.replace("-", "_")
    df.drop('normalized_losses', axis=1, inplace=True)
    df.dropna(inplace=True)

    # fix numeric
    for col in ['bore', 'stroke', 'horsepower', 'peak_rpm', 'price']:
        df[col] = df[col].astype('float')

    # lets replace drive_wheels 4wd with fwd
    df['drive_wheels'].replace('4wd', 'fwd', inplace=True)
    return df


def make_regressor(model_name, model, grid_params, data):
    """Trains and scores models using sklearn GridSearchCV.

    Args:
        model_name (str): the name of the model.
        model (object): the sklearn instance of the model.
        grid_params (dict): the grid parameters for the model.

    Returns:
        tuple: Contains the fitted model, the predictions on the test set and
        a dict containing:

        - 'r2': r2 score
        - 'mse': mse score
        - 'parameters': grid parameters for the best model

    """
    start_time = time.time()
    X_train_proc, y_train, X_test_proc, y_test = data

    # the GridSearchCV
    grid = GridSearchCV(
        model, grid_params,
        scoring='neg_mean_squared_error',
        n_jobs=-1, cv=3
        )
    grid.fit(X_train_proc, y_train)

    # get the best model & params
    model = grid.best_estimator_
    parameters = model.get_params()

    # lets score the model on the test set
    y_predictions = np.exp(model.predict(X_test_proc))
    mse = metrics.mean_squared_error(np.exp(y_test), y_predictions)
    r2 = model.score(X_test_proc, y_test)
    end_time = time.time()
    elapsed = end_time - start_time

    message = f'Score r2: {r2:.4} \nScore MSE: {mse:.4} \nTime: {elapsed:.2}s'
    print(model_name)
    print(message)
    print(parameters)

    stats = {
        'model name': model_name,
        'r2': r2,
        'mse': mse,
        'parameters': parameters,
        'time': elapsed
    }
    return model, y_predictions, stats
