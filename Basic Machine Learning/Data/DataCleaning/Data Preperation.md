

## **Data Cleansing*** 

is the process of analyzing data for finding incorrect, corrupt, and missing values and abluting it to make it suitable for input to data analytics and various machine learning algorithms.

## **Reasons for data corruption:**

-  Data is collected from various structured and unstructured sources and then combined, leading to duplicated and mislabeled values.
-  Different data dictionary definitions for data stored at various locations.
-  Manual entry error/Typos.
-  Incorrect capitalization.
-  Mislabelled categories/classes.

## **Data Quality**

Data Quality is of utmost importance for the analysis. There are several quality criteria that need to be checked upon:

### **Data Quality Attributes**

1. **Completeness** : It is defined as the percentage of entries that are filled in the dataset. The percentage of missing values in the dataset is a good indicator of the quality of the dataset.
2. **Accuracy**: It is defined as the extent to which the entries in the dataset are close to their actual values.
3. **Uniformity**: It is defined as the extent to which data is specified using the same unit of measure.
4. **Consistency**: It is defined as the extent to which the data is consistent within the same dataset and across multiple datasets.
5. **Validity**: It is defined as the extent to which data conforms to the constraints applied by the business rules. There are various constraints:
 
 
 - Data-type Constraints
 - Unique Constraint
 - Mandatory Constraint
 - Range Constraint
 - Regular Expression Constraint


---
### Data Profiling Report

Data Profiling is the process of exploring our data and finding insights from it. Pandas profiling report is the quickest way to extract complete information about the dataset. The first step for data cleansing is to perform exploratory data analysis.

#### **How to use pandas profiling:** 

**Step 1:** The first step is to install the pandas profiling package using the pip command:

```undefined
pip install pandas-profiling
```

**Step 2:** Load the dataset using pandas:

```javascript
import pandas as pd
```

**Step 3**: Read the first five rows:

```scss
df.head()
```

![data](https://editor.analyticsvidhya.com/uploads/95532dataset.png)

Step 4: Generate the profiling report using the following commands:

```csharp
from pandas_profiling 
```

```ini
prof = ProfileReport(df)prof.to_file(output_file='output.html')
```

The profiling report consists of five parts: 

1. **overview, 
2. variables, 
3. interactions,
4. correlation, and 
5. missing values. 
. Overview gives the general statistics about the number of variables, number of observations,  missing values, duplicates, and number of categorical and numeric variables.

. Variable information tells detailed information about the distinct values, missing values, mean, median, etc. Here statistics about a categorical variable and a numerical variable is shown:

-Correlation is defined as the degree to which two variables are related to each other. The profiling report describes the correlation of different variables with each other in form of a **heatmap**.

-Interactions:  This part of the report shows the interactions of the variables with each other. You can select any variable on the respective axes.

