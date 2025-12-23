
## Operations include importing
pd.read_csv()
pd.read_excel()
pd.read_sql()
pd.read_json()
pd.read_html()

## Operations include exporting
df.to_csv()
df.to_excel()
df.to_sql()
df.to_html()

## To inspect data : for summary statistics of numerical columns.

df.head()
df.tail()
df.info()
df.shape()
df.describe()

## To inspect data : for summary statistics of categorical columns.

df.describe(include=['0'])
- `'O'` stands for **Object dtype**
    
- In pandas, **object columns usually mean categorical or text data**
    - Names
    - Cities
    - Gender
    - Product type

|Statistic|Meaning|
|---|---|
|`count`|Number of non-missing values|
|`unique`|Number of distinct categories|
|`top`|Most frequent value|
|`freq`|Frequency of the most common value|
df.columns
df.dtypes

# Missing Values

df.isnull()
df.isna()
df.isnull().sum()
df.isna().sum

df.dropna()
df.dropnill()

df.fillna(value)
df.fillnull(value)

 Data types can be converted using
 df.astype()
 
values can be replaced with
df.replace()

Columns can be renamed with
df.rename(column ={})

The index can be set or reset using
df.set_index()

df.reset_index(drop=True,inplace=True)

Data selection and filtering are performed using

Aggregation and grouping are supported through

For visualization, Pandas integrates with Matplotlib to generate plots directly from DataFrames
Functions include `df.plot.bar()`, `df.plot.line()`, `df.plot.scatter()`, `df.plot.hist()`, `df.plot.box()`, and `df.plot.pie()`. Statistical operations such as `df.mean()`, `df.median()`, `df.std()`, `df.var()`, `df.min()`, `df.max()`, `df.corr()`, and `df.cov()` are available for quick analysis.

### Step 12: Data formatting

Data formatting involves converting the data into a standard format or structure that can be easily processed by the algorithms or models used for analysis. Here we will discuss commonly used data formatting techniques i.e. Scaling and Normalization.

Scaling involves transforming the values of features to a specific range. It maintains the shape of the original distribution while changing the scale. It is useful when features have different scales and certain algorithms are sensitive to the magnitude of the features. Common scaling methods include:

****1. Min-Max Scaling:**** Min-Max scaling rescales the values to a specified range, typically between 0 and 1. It preserves the original distribution and ensures that the minimum value maps to 0 and the maximum value maps to 1.
![[Pasted image 20251223163639.png]]
****2. Standardization (Z-score scaling):**** Standardization transforms the values to have a mean of 0 and a standard deviation of 1. It centers the data around the mean and scales it based on the standard deviation. Standardization makes the data more suitable for algorithms that assume a Gaussian distribution or require features to have zero mean and unit variance.
> Z = (X - μ) / σ

Where,

- X = Data
- μ = Mean value of X
- σ = Standard deviation of X