

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

