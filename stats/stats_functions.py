import pandas as pd
from math import sqrt


def calculate_population_variance(numbers: list):
    mean = sum(numbers) / len(numbers)
    sum_square = 0.0
    print("mean of numbers: " + str(mean))
    for number in numbers:
        difference = (number * 1.0) - mean
        square = difference ** 2
        sum_square += square
    variance = sum_square / len(numbers)
    return variance


def calculate_standard_deviation(numbers: list):
    variance = calculate_population_variance(numbers)
    standard_deviation = sqrt(variance)
    return standard_deviation


def calculate_Q1_Q2_IQR(numbers: list):
    dataframe = pd.DataFrame({'numbers': numbers})
    Q1 = dataframe['numbers'].quantile(0.25)
    Q3 = dataframe['numbers'].quantile(0.75)
    IQR = Q3 - Q1
    return Q1, Q3, IQR


def calculate_upper_fence(Q3, IQR):
    uppper_fence = Q3 + (1.5 * IQR)
    return uppper_fence


def calculate_lower_fence(Q1, IQR):
    lower_fence = Q1 - (1.5 * IQR)
    return lower_fence


def calculate_covariance(x: list, y: list):
    if len(x) != len(y):
        raise ArithmeticError('Length of x must be equal to length of y.')

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    sum_product = 0.0
    for i in range(len(x)):
        difference_x = x[i] - mean_x
        difference_y = y[i] - mean_y
        product = difference_x * difference_y
        sum_product += product

    covariance = sum_product / (len(x) - 1)
    return covariance


def calculate_population_kurtosis(data: list):
    n = len(data)
    mean = sum(data)/n
    sigma = 0
    for i in range(n):
        sigma += (data[i] - mean)**2
    sigma = sigma/n
    kurt = 0
    for i in range(n):
        kurt += (data[i] - mean)**4
    kurt = kurt/n
    kurt = kurt/(sigma**2)
    return kurt


def calculate_kurtosis_sample(data: list):
    """Calculates the sample kurtosis of a dataset using a for loop.
    Important: It's important to note that a sample size should be much larger than this; we are using six numbers to
    reduce the calculation steps. A good rule of thumb is to use 30% of your data for populations under 1,000.
    For larger populations, you can use 10%.
    Args:
      data (list): List of numerical values.
    Returns:
      float: The sample kurtosis of the dataset.
    """
    kurt = calculate_population_kurtosis(data)
    kurt = kurt - 3
    return kurt

