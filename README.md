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

**covariance** 

It is the measure of how much two variables change together.

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/covariance_formula.png)

There are 3 types of covariance.

These are:

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/positive_covariance.png)

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/negative_covariance.png)

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/zero_covariance.png)

Try to run [covariance.py](https://github.com/AyberkYavuz/statistics/blob/main/covariance.py) to calculate the covariance of x and y.

**Example Run**
```bash
enter x list elements: 8 10 12 14
enter y list elements: 2.1 2.5 3.6 4.0
Calculating covariance
covariance: 2.2666666666666666
```

* A large covariance can mean a strong relationship between variables.
* You can't compare variances over data sets (variables) with different scales like pounds and inches.
* The wide range of results makes it hard to interpret.
    * For example; your variables could return a value of 3 or 3.000.
    * The larger the x and y values, the larger the covariance.
    * Fix: Corr(x,y) = Cov(x,y) / (std_x * std_y)
        * std_x: standard deviation of x
        * std_y: standard deviation of y

Try to run [correlation.py](https://github.com/AyberkYavuz/statistics/blob/main/correlation.py) to calculate the correlation of x and y.

**Example Run**
```bash
enter x list elements: 43 21 25 42 57 59
enter y list elements: 99 65 79 75 87 81
Calculating covariance
covariance: 95.6
Calculating standard deviation of x
mean of numbers: 41.166666666666664
standard_deviation_x: 14.380735570740306
Calculating standard deviation of y
mean of numbers: 81.0
standard_deviation_y: 10.456258094238748
Calculating correlation
correlation: 0.6357706822682092
```

**correlation coefficients**

Correlation coefficients are used to measure how strong a relationship is between two variables. There are several types of correlation coefficient, but the most popular is Pearson’s. Pearson’s correlation (also called Pearson’s R) is a correlation coefficient commonly used in linear regression.

**advantages of correlation**

* Covariance can take any numbers; correlation is limited to: -1 to 1.
    * Values always range from -1 for a perfectly inverse, or negative, relationship to 1 for a perfectly positive correlation. Values at, or close to, zero indicate no linear relationship or a very weak correlation.
* Correlation is more useful for determining the relationship strength.
* Correlation does not have units. Covariance always has units.
* Correlation isn't affected by changes in the center.

**disadvantage of the correlation**

* It only measures linear relationhips between X and Y and for any relationship to exist, any change in X has to have a constant proportional change in Y. If the relationship is not linear then the result is inaccurate. 

**alpha level (significance level)**

The significance level or alpha level is the probability of making the wrong decision when the null hypothesis is true. Alpha levels (sometimes just called “significance levels”) are used in hypothesis tests. Usually, these tests are run with an alpha level of .05 (5%), but other levels commonly used are .01 and .10.

**One Sample T Test**

The one sample t test compares the mean of your sample data to a known value. For example, you might want to know how your sample mean compares to the population mean. You should run a one sample t test when you don’t know the population standard deviation or you have a small sample size. For a full rundown on which test to use, see: T-score vs. Z-Score.

Assumptions of the test (your data should meet these requirements for the test to be valid):

* Data is independent.
* Data is collected randomly. For example, with simple random sampling.
* The data is approximately normally distributed.

**Example question:** your company wants to improve sales. Past sales data indicate that the average sale was $100 per transaction. After training your sales force, recent sales data (taken from a sample of 25 salesmen) indicates an average sale of $130, with a standard deviation of $15. Did the training work? Test your hypothesis at a 5% alpha level.

**Step 1:** Write your null hypothesis statement (How to state a null hypothesis). The accepted hypothesis is that there is no difference in sales, so:
H0: μ = $100.

**Step 2:** Write your alternate hypothesis. This is the one you’re testing in the one sample t test. You think that there is a difference (that the mean sales increased), so:
H1: μ > $100.

**Step 3:** Identify the following pieces of information you’ll need to calculate the test statistic. The question should give you these items:

1. The sample mean(x̄). This is given in the question as $130.
2. The population mean(μ). Given as $100 (from past data).
3. The sample standard deviation(s) = $15.
4. Number of observations(n) = 25.

**Step 4:** Insert the items from above into the t score formula.

![alt text](https://github.com/AyberkYavuz/statistics/blob/main/imgs/t_score_formula.png)

t = (130 – 100) / ((15 / √(25))
t = (30 / 3) = 10

This is your **calculated t-value**.

**Step 5:** Find the t-table value. You need two values to find this:

The alpha level: given as 5% in the question.
The degrees of freedom, which is the number of items in the sample (n) minus 1: 25 – 1 = 24.

**T-Distribution Table (One Tail)**

df	a = 0.1	0.05	0.025	0.01	0.005	0.001	0.0005
∞	ta = 1.282	1.645	1.960	2.326	2.576	3.091	3.291
1	3.078	6.314	12.706	31.821	63.656	318.289	636.578
2	1.886	2.920	4.303	6.965	9.925	22.328	31.600
3	1.638	2.353	3.182	4.541	5.841	10.214	12.924
4	1.533	2.132	2.776	3.747	4.604	7.173	8.610
5	1.476	2.015	2.571	3.365	4.032	5.894	6.869
6	1.440	1.943	2.447	3.143	3.707	5.208	5.959
7	1.415	1.895	2.365	2.998	3.499	4.785	5.408
8	1.397	1.860	2.306	2.896	3.355	4.501	5.041
9	1.383	1.833	2.262	2.821	3.250	4.297	4.781
10	1.372	1.812	2.228	2.764	3.169	4.144	4.587
11	1.363	1.796	2.201	2.718	3.106	4.025	4.437
12	1.356	1.782	2.179	2.681	3.055	3.930	4.318
13	1.350	1.771	2.160	2.650	3.012	3.852	4.221
14	1.345	1.761	2.145	2.624	2.977	3.787	4.140
15	1.341	1.753	2.131	2.602	2.947	3.733	4.073
16	1.337	1.746	2.120	2.583	2.921	3.686	4.015
17	1.333	1.740	2.110	2.567	2.898	3.646	3.965
18	1.330	1.734	2.101	2.552	2.878	3.610	3.922
19	1.328	1.729	2.093	2.539	2.861	3.579	3.883
20	1.325	1.725	2.086	2.528	2.845	3.552	3.850
21	1.323	1.721	2.080	2.518	2.831	3.527	3.819
22	1.321	1.717	2.074	2.508	2.819	3.505	3.792
23	1.319	1.714	2.069	2.500	2.807	3.485	3.768
24	1.318	1.711	2.064	2.492	2.797	3.467	3.745
25	1.316	1.708	2.060	2.485	2.787	3.450	3.725
26	1.315	1.706	2.056	2.479	2.779	3.435	3.707
27	1.314	1.703	2.052	2.473	2.771	3.421	3.689
28	1.313	1.701	2.048	2.467	2.763	3.408	3.674
29	1.311	1.699	2.045	2.462	2.756	3.396	3.660
30	1.310	1.697	2.042	2.457	2.750	3.385	3.646
60	1.296	1.671	2.000	2.390	2.660	3.232	3.460
120	1.289	1.658	1.980	2.358	2.617	3.160	3.373

**Resources**

https://www.youtube.com/watch?v=LMz2ouNcXUQ&ab_channel=Intellipaat

https://www.scribbr.com/statistics/outliers/

https://www.investopedia.com/terms/s/standard-error.asp

https://www.investopedia.com/terms/d/degrees-of-freedom.asp

https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/#definition

https://study.com/academy/lesson/covariance-correlation-equations-examples.html#:~:text=The%20correlation%20coefficient%20can%20be%20calculated%20as%20follows%3A,%CF%83%20x%20%E2%88%97%20%CF%83%20y%20)

https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/what-is-an-alpha-level/

https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/one-sample-t-test/
