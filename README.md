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

**5 number summary**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/5_number_summary.png)

**box plot**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/box_plot.png)

**symmetric distribution**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/symmetric_distribution.png)

**the relationship between mean and median in normal distribution**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/mean_meadian_normal_distribution.png)

**bell curve distribution**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/bell_curve_distribution.png)

**standard error:** The standard error (SE) of a statistic is the approximate standard deviation of a statistical sample population.

The standard error is a statistical term that measures the accuracy with which a sample distribution represents a population by using standard deviation. In statistics, a sample mean deviates from the actual mean of a population; this deviation is the standard error of the mean.

* The standard error (SE) is the approximate standard deviation of a statistical sample population.
* The standard error describes the variation between the calculated mean of the population and one which is considered known, or accepted as accurate.
* The more data points involved in the calculations of the mean, the smaller the standard error tends to be.

**margin of error:** The margin of error (MOE) for a survey tells you how near you can expect the survey results to be to the correct population value. For example, a survey indicates that 72% of respondents favor Brand A over Brand B with a 3% margin of error. In this case, the actual population percentage that prefers Brand A likely falls within the range of 72% ± 3%, or 69 – 75%.

**standard error and margin of error relation**

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/standard_error_and_margin_of_error.png)

**degrees of freedom**

* Degrees of freedom refers to the maximum number of logically independent values, which are values that have the freedom to vary, in the data sample.
* Degrees of freedom is calculated by subtracting one from the number of items within the data sample.

df = n -1

df = degrees of freedom

n = sample size

**covariance:** It is the measure of how much two variables change together.

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/covariance_formula.png)

Resources

https://www.youtube.com/watch?v=LMz2ouNcXUQ&ab_channel=Intellipaat

https://www.scribbr.com/statistics/outliers/

https://www.investopedia.com/terms/s/standard-error.asp

https://www.investopedia.com/terms/d/degrees-of-freedom.asp

https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/#definition
