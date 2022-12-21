from stats.stats_functions import calculate_Q1_Q2_IQR
from stats.stats_functions import calculate_upper_fence
from stats.stats_functions import calculate_lower_fence

numbers = [int(x) for x in input("enter numbers: ").split()]
numbers.sort()

print("Calculating Q1, Q2, IQR")
Q1, Q3, IQR = calculate_Q1_Q2_IQR(numbers)

print("Calculating upper fence")
uppper_fence = calculate_upper_fence(Q3, IQR)

print("Calculating lower fence")
lower_fence = calculate_lower_fence(Q1, IQR)

print("Finding larger extreme values")

larger_extreme_values = list(filter(lambda number: number > uppper_fence, numbers))
print("larger extreme values: " + str(larger_extreme_values))

print("Finding smaller extreme values")

smaller_extreme_values = list(filter(lambda number: number < lower_fence, numbers))
print("smaller extreme values: " + str(smaller_extreme_values))
