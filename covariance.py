from stats.stats_functions import calculate_covariance

x = [float(x) for x in input("enter x list elements: ").split()]
y = [float(y) for y in input("enter y list elements: ").split()]

print("Calculating covariance")
covariance = calculate_covariance(x, y)
print("covariance: " + str(covariance))

