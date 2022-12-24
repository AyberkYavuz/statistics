from stats.stats_functions import calculate_kurtosis_sample
from scipy.stats import kurtosis

data = [float(x) for x in input("enter data points: ").split()]

print("Calculating Kurtosis for Sample")
kurtosis = calculate_kurtosis_sample(data)

print("kurtosis: " + str(kurtosis))

print("scipy.stats kurtosis function result: " + str(kurtosis(data)))

