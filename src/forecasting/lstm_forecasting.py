# LSTM Forecasting
from keras.models import Sequential
from keras.layers import LSTM, Dense

def build_lstm_model(input_shape):
    """Build an LSTM model."""
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model