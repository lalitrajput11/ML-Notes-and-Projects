# Numpy Tutorial For Beginners 

NumPy (or Numpy) is a Linear Algebra Library for Python.
import numpy as np

def calculate_statistics(data):
    """
    Calculate basic statistics (mean, median, standard deviation) of a given list of numbers.

    Parameters:
    data (list or np.ndarray): A list or numpy array of numerical values.

    Returns:
    dict: A dictionary containing the mean, median, and standard deviation.
    """
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("Input data must be a list or numpy array.")

    data_array = np.array(data)

    statistics = {
        'mean': np.mean(data_array),
        'median': np.median(data_array),
        'std_dev': np.std(data_array)
    }

    return statistics

