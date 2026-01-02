# Risk Feature Engineering

def calculate_volatility(df, column, window):
    """Calculate rolling volatility for a given column."""
    df[f"{column}_volatility"] = df[column].rolling(window=window).std()
    return df