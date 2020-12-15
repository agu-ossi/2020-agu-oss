"""A few helper utilities."""

import numpy as np

def divide(a, b):
    """Divide two numbers.

    Parameters
    ----------
    a : int, float
        The dividend

    b : int, float
        The divisor

    Return
    ------
    int, float: the quotient

    """
    return a / b


def moving_average(data, window_size):
    """
    Calculate a moving average over 1D data using the given window size.

    Parameters
    ----------
    data : numpy.ndarray
           Data that we will compute the moving average over

    window_size : int
                  width of the window we use to compute the moving average

    """
    average = np.full(data.size, np.nan)
    half_window = window_size // 2
    for i in range(half_window, data.size - half_window):
        average[i] = np.mean(data[i - half_window: i + window_size-half_window])
    return average
