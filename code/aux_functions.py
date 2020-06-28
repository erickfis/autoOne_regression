"""
# Project AutoOne_regression

Auxiliary functions for cleanning data and building regression models

- Erick Medeiros Anastácio
- 2020-06-28
- Python 3.7

"""

import pandas as pd
import numpy as np


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
