# Development Feature Engineering

def calculate_growth_rate(df, column):
    """Calculate growth rate for a given column."""
    df[f"{column}_growth_rate"] = df[column].pct_change()
    return df