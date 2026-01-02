# Data Cleaning Utilities
import pandas as pd

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    return df.fillna(method='ffill').fillna(method='bfill')