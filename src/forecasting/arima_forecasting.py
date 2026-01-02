# ARIMA Forecasting
from statsmodels.tsa.arima.model import ARIMA

def forecast_with_arima(data, order):
    """Forecast using ARIMA model."""
    model = ARIMA(data, order=order)
    fitted_model = model.fit()
    return fitted_model.forecast(steps=5)