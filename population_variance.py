from stats.stats_functions import calculate_population_variance

numbers = [int(x) for x in input("enter numbers: ").split()]

print("Calculating variance of numbers")
variance = calculate_population_variance(numbers)
print("variance of numbers: " + str(variance))


