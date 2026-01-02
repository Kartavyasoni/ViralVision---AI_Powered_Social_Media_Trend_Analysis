# Data Transformation Utilities
import pandas as pd

def normalize_data(df, columns):
    """Normalize specified columns in the dataset."""
    for column in columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df