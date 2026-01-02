# Plotting Utilities
import matplotlib.pyplot as plt

def plot_time_series(data, x, y, title):
    """Plot a time series graph."""
    plt.figure(figsize=(10, 6))
    plt.plot(data[x], data[y])
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()