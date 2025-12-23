## Step 4: Exploratory Data Analysis (EDA)

To find patterns and characteristics hidden in the data Exploratory Data Analysis (EDA) is used to uncover insights and understand the dataset's structure. During EDA patterns, trends and insights are provided which may not be visible by naked eyes. This valuable insight can be used to make informed decision.

Here are the basic features of Exploratory Data Analysis:

- ****Exploration:**** Use statistical and visual tools to explore patterns in data.
- ****Patterns and Trends:**** Identify underlying patterns, trends and potential challenges within the dataset.
- ****Insights:**** Gain valuable insights for informed decisions making in later stages.
- ****Decision Making:**** Use EDA for feature engineering and model selection.
## Why Exploratory Data Analysis Important

1. Helps to understand the dataset by showing how many features it has, what type of data each feature contains and how the data is distributed.
2. Helps to identify hidden patterns and relationships between different data points which help us in and model building.
3. Allows to identify errors or unusual data points (outliers) that could affect our results.
4. The insights gained from EDA help us to identify most important features for building models and guide us on how to prepare them for better performance.
5. By understanding the data it helps us in choosing best modeling techniques and adjusting them for better results

## Types of Exploratory Data Analysis

There are various types of EDA based on nature of records. Depending on the number of columns we are analyzing we can divide EDA into three types:

### 1. Univariate Analysis

[Univariate analysis](https://www.geeksforgeeks.org/data-visualization/what-is-univariate-bivariate-multivariate-analysis-in-data-visualisation/) focuses on studying one variable to understand its characteristics. It helps to describe data and find patterns within a single feature. Various common methods like histograms are used to show data distribution, box plots to detect outliers and understand data spread and bar charts for categorical data. Summary statistics like [****mean****,](https://www.geeksforgeeks.org/dsa/mean/) [****median****](https://www.geeksforgeeks.org/maths/median/), [****mode****](https://www.geeksforgeeks.org/maths/what-is-mode/), [****variance****](https://www.geeksforgeeks.org/maths/variance/) and [****standard deviation****](https://www.geeksforgeeks.org/maths/standard-deviation-formula/) helps in describing the central tendency and spread of the data


import pandas as pd
import seaborn as sns
data = pd.read_csv('Employee_dataset.csv')
print(data.head())

### Histogram

Here we’ll be performing univariate analysis on Numerical variables using the histogram.
sns.histplot(data['age'])

### Bar Chart

Univariate analysis of categorical data. We’ll be using the _count plot_ function from the _seaborn_ library

sns.countplot(data['gender_full'])

### Pie Chart

A piechart helps us to visualize the percentage of the data belonging to each category.
x = data['STATUS_YEAR'].value_counts()
plt.pie(x.values,
        labels=x.index,
        autopct='%1.1f%%')
plt.show()
### ****2. Bivariate Analysis****

[Bivariate Analysis](https://www.geeksforgeeks.org/maths/bivariate-analysis/) focuses on identifying relationship between two variables to find connections, correlations and dependencies. It helps to understand how two variables interact with each other. Some key techniques include:

- Scatter plots which visualize the relationship between two continuous variables.
- Correlation coefficient measures how strongly two variables are related which commonly use [****Pearson's correlation****](https://www.geeksforgeeks.org/maths/pearson-correlation-coefficient/) for linear relationships.
- Cross-tabulation or contingency tables shows the frequency distribution of two categorical variables and help to understand their relationship.
- ****Line graphs**** are useful for comparing two variables over time in time series data to identify trends or patterns.
- [****Covariance****](https://www.geeksforgeeks.org/engineering-mathematics/mathematics-covariance-and-correlation/) measures how two variables change together but it is paired with the correlation coefficient for a clearer and more standardized understanding of the relationship.

### 3. Multivariate Analysis

[Multivariate Analysis](https://www.geeksforgeeks.org/r-language/multivariate-analysis-in-r/) identify relationships between two or more variables in the dataset and aims to understand how variables interact with one another which is important for statistical modeling techniques. It include techniques like:

- [****Pair plots****](https://www.geeksforgeeks.org/data-visualization/python-seaborn-pairplot-method/) which shows the relationships between multiple variables at once and helps in understanding how they interact.
- Another technique is [****Principal Component Analysis (PCA****](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)****)**** which reduces the complexity of large datasets by simplifying them while keeping the most important information.
- [****Spatial Analysis****](https://www.geeksforgeeks.org/data-science/what-is-spatial-analysis/) is used for geographical data by using maps and spatial plotting to understand the geographical distribution of variables.
- [****Time Series Analysis****](https://www.geeksforgeeks.org/data-analysis/time-series-data-visualization-in-python/) is used for datasets that involve time-based data and it involves understanding and modeling patterns and trends over time. Common techniques include line plots, autocorrelation analysis, moving averages and [ARIMA](https://www.geeksforgeeks.org/machine-learning/python-arima-model-for-time-series-forecasting/) models.

## Steps for Performing Exploratory Data Analysis

It involves a series of steps to help us understand the data, uncover patterns, identify anomalies, test hypotheses and ensure the data is clean and ready for further analysis. It can be done using different tools like:

- In Python, Pandas is used to clean, filter and manipulate data. [Matplotlib](https://www.geeksforgeeks.org/data-visualization/data-visualization-using-matplotlib/) helps to create basic visualizations while [Seaborn](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) makes more attractive plots. For interactive visualizations Plotly is a good choice.
- In R, ****ggplot2**** is used for creating complex plots, ****dplyr**** helps with data manipulation and ****tidyr**** makes sure our data is organized and easy to work with.

https://www.geeksforgeeks.org/data-visualization/plotting-histogram-in-python-using-matplotlib/
https://www.geeksforgeeks.org/data-visualization/what-is-univariate-bivariate-multivariate-analysis-in-data-visualisation/
https://www.geeksforgeeks.org/machine-learning/machine-learning-lifecycle/
