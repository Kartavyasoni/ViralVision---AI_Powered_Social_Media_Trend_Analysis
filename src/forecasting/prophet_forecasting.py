# Prophet Forecasting
from prophet import Prophet

def forecast_with_prophet(df, date_col, value_col):
    """Forecast using Prophet model."""
    df = df.rename(columns={date_col: 'ds', value_col: 'y'})
    model = Prophet()
    model.fit(df)
    return model.predict(df)