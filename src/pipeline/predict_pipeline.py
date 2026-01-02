# Prediction Pipeline
from src.forecasting.prophet_forecasting import forecast_with_prophet

def run_prediction_pipeline():
    """Run the prediction pipeline."""
    # Example steps
    data = {"ds": [], "y": []}  # Replace with actual data
    forecast = forecast_with_prophet(data, "ds", "y")
    return forecast
