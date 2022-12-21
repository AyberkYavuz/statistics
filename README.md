# statistics
This repository is for containing sources codes of statistical concepts like outlier detection, etc.

**population:** It is a large volume of observations.

**sample:**  It is a small portion of that population. Using these sample statistics, we make conclusions about the population.

**mean:** It is the average of a collection of values. We can calculate the mean by dividing the sum of all observations by the number of observations.

**variance:** It is a statistical measurement of the spread between numbers in a data set. More specifically, variance measures how far each number in the set is from the mean (average), and thus from every other number in the set. Variance is often depicted by this symbol: σ2.

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/sample_variance_formula_image.png?raw=true)

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/population_variance_formula_image.png?raw=true)

Try to run [population_variance.py](https://github.com/AyberkYavuz/statistics/blob/main/population_variance.py) to calculate the population variance of the given numbers.

**Example Run**
```bash
enter numbers: 2 7 3 12 9
Calculating variance of numbers
mean of numbers: 6.6
variance of numbers: 13.84
```

**standard deviation:** It is simply the square root of the variance. Standard deviation is useful when comparing the spread of two separate data sets that have approximately the same mean. The data set with the smaller standard deviation has a narrower spread of measurements around the mean and therefore usually has comparatively fewer high or low values. An item selected at random from a data set whose standard deviation is low has a better chance of being close to the mean than an item from a data set whose standard deviation is higher. However, standard deviation is affected by extreme values. A single extreme value can have a big impact on the standard deviation.

Try to run [standard_deviation.py](https://github.com/AyberkYavuz/statistics/blob/main/standard_deviation.py) to calculate the standard deviation of the given numbers.

**Example Run**
```bash
enter numbers: 2 7 3 12 9
Calculating standard deviation of numbers
mean of numbers: 6.6
standard_deviation of numbers: 3.7202150475476548
```

**descriptive statistics:** provides exact and accurate information.

**inferential statistics:** It is used to draw conclusions about a population using some sample data.

**quantitative data:** numeric data.

**qualitative data:** categorical data.

**outlier:** It is either much larger or much smaller than other values in the collection.

**outlier detection**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/outlier_detection.png?raw=true)

This method is helpful if you have a few values on the extreme ends of your dataset, but you aren’t sure whether any of them might count as outliers.

**Interquartile range method**

1. Sort your data from low to high
2. Identify the first quartile (Q1), the median, and the third quartile (Q3).
3. Calculate your IQR = Q3 – Q1
4. Calculate your upper fence = Q3 + (1.5 * IQR)
5. Calculate your lower fence = Q1 – (1.5 * IQR)
6. Use your fences to highlight any outliers, all values that fall outside your fences.

Your outliers are any values greater than your upper fence or less than your lower fence.

Try to run [outlier_detection.py](https://github.com/AyberkYavuz/statistics/blob/main/outlier_detection.py) to detect outliers of the given numbers.

**Example Run**
```bash
enter numbers: 25 37 24	28 35 22 31 53 41 64 29
Calculating Q1, Q2, IQR
Calculating upper fence
Calculating lower fence
Finding larger extreme values
larger extreme values: [64]
Finding smaller extreme values
smaller extreme values: []
```

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/5_number_summary.png)

Resources

https://www.youtube.com/watch?v=LMz2ouNcXUQ&ab_channel=Intellipaat

https://www.scribbr.com/statistics/outliers/
