from stats.stats_functions import calculate_covariance
from stats.stats_functions import calculate_standard_deviation

x = [float(x) for x in input("enter x list elements: ").split()]
y = [float(y) for y in input("enter y list elements: ").split()]

print("Calculating covariance")
covariance = calculate_covariance(x, y)
print("covariance: " + str(covariance))

print("Calculating standard deviation of x")
standard_deviation_x = calculate_standard_deviation(x)
print("standard_deviation_x: " + str(standard_deviation_x))

print("Calculating standard deviation of y")
standard_deviation_y = calculate_standard_deviation(y)
print("standard_deviation_y: " + str(standard_deviation_y))

print("Calculating correlation")
correlation = covariance / (standard_deviation_x * standard_deviation_y)

print("correlation: " + str(correlation))

