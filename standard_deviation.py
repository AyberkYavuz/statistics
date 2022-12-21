from stats.stats_functions import calculate_population_variance
from math import sqrt

numbers = [int(x) for x in input("enter numbers: ").split()]

print("Calculating standard deviation of numbers")
variance = calculate_population_variance(numbers)
standard_deviation = sqrt(variance)
print("standard_deviation of numbers: " + str(standard_deviation))

