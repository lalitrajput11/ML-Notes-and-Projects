# word = input("Enter a word: ").strip()
# count = int(input("How many times to repeat it? "))

# # Create the repeated string with commas
# result = (word + ", ") * (count - 1) + word   # adds comma after all except the last one

# print("\nResult:")
# print(result)
# word ="We"
# list =[]
# for i in range(4):
#     list.append(word)
# print(list)

# li1 = [word for i in range(5)] 
# print(li1)

# li1 = [i for i in range(11)]
# print(li1)

# l1 = [i**2 for i in range(1,11)]
# l1 = [i for i in range(1,21) if i%2 !=0]
# l1 =[1,2,3,4]
# l2 = [str(x) for x in l1]
# print(l2)

# a = [1, 2, 3, 4, 5]

# # Convert each element using a list comprehension
# b = [str(x) for x in a]

# print(b)

# l1 =[1,2,3,4]
# l2 =list(map(str,l1))
# print(l2)'

# l1 ="sdkdnkl"
# l2 = ''.join(reversed(l1))
# l3 =[char for char in l1]
# print(l2)
# print(l3)
# l2 =[i for i in range(1,101) if i%5==0]
# print(l2)

# w =["apple", "banana", "cherry", "date"]
# w = [word.capitalize() for word in w]
# print(w)

# e =['a','b','c','d']
# e = [char.upper() for char in e]
# print(e)

w =["apple", "banana", "cherry", "date"]
# i want to upper case every alphabet in the words
# w = [''.join([char.upper() for char in word]) for word in w]
# print(w)

# w =[''.join([char.upper() for char in word]) for word in w]
# print(w)

# l1 =['APPLE', 'BANANA', 'CHERRY', 'DATE']


# l2 =[len(word) for word in l1]
# print(l2)

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 =[i**2 for i in l1 if i%2==0]
# print(l2)

# s = 'applekwe'

# l1 = [char for char in s if char in "aeiouAEIOU"]
# print(l1)

# Design a class SeriesCalculator that calculates the sum of an arithmetic series

# class SeriesCalculator:
#     def __init__(self,series):
#         self.series = series
        
#     def SumAP(self):
#         if not self.series:
#             return "List is empty"
#         else :
#             # return sum(self.series)
#             sum =0
#             for i in self.series:
#                 sum+=i
#             return sum
# d =SeriesCalculator([1,2,3,4,5])
# print(d.SumAP())

# class Employee:
#     def __init__(self,name, id=None, Dept=None):
#         self.name =name
#         self.id =id
#         self.Dept =Dept
        
#     def details(self):
#         print(f"Name : {self.name}")
        
#         if self.id:
#             print(f"Id : {self.id}")
            
#         if self.Dept:
#             print(f"Department : {self.Dept}")
# e1 = Employee("John")
# e1.details()
        
# e2 = Employee("KK",1)
# e2.details()

# e3 = Employee("kk",3,"Elect")
# e3.details()

# class Employee:
#     def __init__(self, name, id=None, dept=None):
#         self.name = name
#         self.id = id
#         self.dept = dept
        
#     def details(self):
#         print(f"Name : {self.name}")
        
#         if self.id is not None:
#             print(f"Id : {self.id}")
            
#         if self.dept is not None:
#             print(f"Department : {self.dept}")

# e = Employee("John")
# e.details()

# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "Whoof!"
    
# class cat(Animal):
#     def speak(self):
#         return "mEOW!"
    
# animal1 = Dog()
# animal2 = cat()

# print(animal2.speak())
# print(animal1.speak())


# class Animal:
#     def __init__(self,name):
#         self.name = name 
        
#     def speak(self):
#         print("Generic Animal Sound")
        
# class Dog(Animal):
#     def speak(self):
#         print("Whhop")
        
# m1 = Dog("Pan")
# m1.speak()

# class ParentClass:
#     def __init__(self,name):
#         self.name = name 
        
#     def greet(self):
#         print(f"Hello, my_name is {self.name}")
        
# class ChildClass(ParentClass):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def introduce(self):
#         super().greet
#         print(f"I 'm {self.age} years old")
        
# m1 = ChildClass("lil",24)
# m1.introduce()
# m1.greet()

# def fibonacci_up_to_n(n):
#     if n < 0:
#         return []
#     series = [0, 1]
#     while True:
#         next_num = series[-1] + series[-2]
#         if next_num > n:
#             break
#         series.append(next_num)
#     return series if n >= 0 else []

# # Read input
# num = int(input())
# result = fibonacci_up_to_n(num)
# print(" ".join(map(str, result)))

# def lengthOfLongestSubstring(s):
#     char_set = set()
#     left = right = 0
#     max_len = 0
    
#     while right < len(s):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#         right += 1
#     return max_len

# # Test
# print(lengthOfLongestSubstring("abcabcbb"))  # 3

import sklearn
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid")


# iris = load_iris()
# x = iris.data
# y = iris.target
# df = pd.DataFrame(iris)


df = load_iris(as_frame=True).frame

# print(df.head())
# print(df.info)
# print(df.shape)

# print(df.describe)

# print(df.isnull().sum())
# print(df.duplicated().sum())

# print(df[df.duplicated(keep=False)])

# print(df[df.duplicated()].index)
# print(df.loc[df.duplicated(keep = False)])

df_clean = df.drop_duplicates()

# print(df_clean.duplicated().sum())

# print(df_clean.head(2))

# df_clean['target'].value_counts()
# plt.figure()

# df['target'].value_counts().plot(kind='bar')
# plt.title("Species Distribution")
# plt.xlabel("Species")
# plt.ylabel("Count")

# plt.show()
# feature_names = iris.feature_names
# target_names = iris.target_names

from sklearn.model_selection import train_test_split
X = df_clean.drop(columns='target')
y = df_clean['target']





X_train,X_test ,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42, stratify=y)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaeld = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

lr = LogisticRegression(max_iter=200)
lr.fit(X_train_scaeld,y_train)

y_pred_lr = lr.predict(X_test_scaled)

print("Logistic Regression Accuracy : ",accuracy_score(y_test,y_pred_lr))
print('Classifiaction_report : ',classification_report(y_test,y_pred_lr))




