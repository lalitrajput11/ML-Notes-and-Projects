# import pandas as pd

# s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
# print(s)

# data = {'Country': ['Belgium',  'India',  'Brazil'],

# 'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

# 'Population': [11190846, 1303171035, 207847528]} 

# df1 = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
# print(df1)

import pandas as pd 
df = pd.read_csv('/home/lalitrajput/Tools/ML-Notes-and-Projects/Basic Machine Learning/Data/DataCleaning/Titanic-Dataset.csv')
# print(df.head())

# df.info()
# print(df.shape)
# print(df.describe())
# print(df.size)

# print(df['Age'].isnull().sum())
# print(df['Age'].fillna(df['Age'].mean(),inplace=True))
# print(df.columns)

# print(df.duplicated())
# print(df.duplicated().sum())

# print(col for col in df.columns.dtype)
cat_col = [col for col in df.columns if df[col].dtype == 'object' ]
# print(cat_col)
num_col = [col for col in df.columns if df[col].dtype != 'object']
# print(num_col)

# print(df[cat_col].nunique())
# print(df.isnull().sum())

df1 = df.drop(columns=['Name',"Cabin",'Ticket'])
df1.dropna(subset=['Embarked'],inplace=True)
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())

# df1['Age'].fillna(df1['Age'].mean(),inplace =True)

# print(df1.describe)

# print(df1.duplicated().sum())
# print(df1.isnull().sum())

import matplotlib as plt 

# plt.boxplot(df1['Age'],vert=False)
# plt.ylabel('Variable')
# plt.xpabel('Age')
# plt.title("Age Distribution Box Plot")
# plt.show()
import matplotlib.pyplot as plt

# plt.boxplot(df1['Age'], vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title('Box Plot')
# plt.show()


mean = df1['Age'].mean()
std = df1['Age'].std()

lower_bound = mean -2*std
upper_bound = mean+2*std

df2 = df1[(df1['Age'] >=lower_bound) & (df1['Age']<=upper_bound)]

df3 = df2.fillna(df2['Age'].mean())
# print(df3.isnull().sum())

# plt.boxplot(df3['Age'],vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title("BoxPlot")
# plt.show()

mean1 = df3['Age'].mean()
std1 = df['Age'].std()

lower_bound1 = mean1 - 2*std1
upper_bound1 = mean1 + 2*std1

df4 = df3[(df3['Age']>=lower_bound1) & (df3['Age']<=upper_bound1)]
# print(df4.isnull().sum())
# plt.boxplot(df4['Age'], vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title('Box Plot After Removing Outliers')  
# plt.show()   

print(df4.columns)
X = df3[(['PassengerId','Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
       'Fare', 'Embarked'])]
Y = df3['Survived']

# from sklearn.model_selection import train_test_split

# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder

# from sklearn.preprocessing import MinMaxScaler

# scaler = MinMaxScaler
# num_col = [col for col in x.columns if x[col].dtype != 'object']

# x1 = x.copy()
# x1[num_col]= scaler.fit_transform(x1[num_col])
# print(x1.head())

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X.copy()
x1[num_col_] = scaler.fit_transform(x1[num_col_])
print(x1.head())

