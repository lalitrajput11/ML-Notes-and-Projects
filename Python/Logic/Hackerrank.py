##############################################################
# https://www.geeksforgeeks.org/quizzes/python-list-quiz/

'''records = []
n = int(input())

for _ in range(n):
    name, score = input().split()
    score = float(score)
    records.append([name, score])
    # name = input()
    # score = float(input())
    # records.append([name, score])
    
grades =[students[1] for students in records]
print(grades)
secnd_lowest = sorted(set(grades))[1] 
print(secnd_lowest)

result = [students for students in records if students[1] == secnd_lowest]
for name in sorted(result):
    print(name[0])'''

################################################################

'''words =[]

n = int(input())
for i in range(n):
    name = input()
    grad = float(input())
    words.append([name,grad])
    
grades = [gr[1] for gr in words]
secnd_lowest = sorted(grades)[1]

res = [student for student in words if student[1]==secnd_lowest]

for name in sorted(res):
    print(name[0])
'''

###################################################################################

# a = [1,2,3]
# a.insert(2,2)
# print(a)

# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 

# pos = nameList.index("Harsh") 

# print (pos * 3)

# a =[]
# a.append([1,[2,4],3])
# a.append([5,6])
# a.extend([55])
# print(a)

# a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if
# (x in ([x for x in range(20)]))] 
# print(a)

# a = [x for x in (x for x in 'Geeks 22966 for Geeks')] 
# print(a)

# a = [int(x) for x in 'Geeks 22966 for Geeks' if x.isdigit()]
# print(a)
# a = [x for x in 'Geeks 22966 for Geeks'] 
# print(a)

# li = ['a', 'b', 'c'] * 0
# print(li)
# a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
# b = a 
# c = a[:] 
# print(c)

# a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
# b = a 
# c = a[:] 

# b[0] = 'Code'
# c[1] = 'Mcq'

# count = 0
# for c in (a, b, c): 
# 	if c[0] == 'Code': 
# 		count += 1
# 	if c[1] == 'Mcq': 
# 		count += 10

# b = [10, 20, 30, 40] 
# c =[i+10 for i in b ]
# print(c)

# a = ['Wkk','dfsf',"fder"]
# b = [i.capitalize() for i in a]
# print(b)

# b = [word[0:len(word)].upper() for word in a]
# print(b)

# a =[1,2,3,4,5]
# b = [3,4,5,6,7]
# d =[]
# for a,b in zip(a,b):
#     item = a+b
#     d.append(item)
# print(d)

# li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# num = [x for x in li if type(x)==int or type(x)==float]
# char = [x for ]


# print(list(zip([1,2,3], [10,20])))
# a =[1,2,3]
# b =[10,20]

# print(list(zip(a, b)))


# a = ['10', '20', '30', '40']
# b = list(map(int,a))
# print(b)

# Square all numbers in a list using map().
# a  = [1,2,3,4]
# b = list(map(lambda x : x**2 , a))
# print(b)


# Convert a list of temperatures from Celsius to Fahrenheit using map().
# celsius = [0, 10, 20, 34.5]
# far = list(map(lambda x : 9/5*x +32 , celsius))
# print(far)

# a =[12,15,20,25,30]
# b = list(filter(lambda x : x%10==0 , a))
# print(b)

# a =[12,15,20,25,30]
# b = [12,15,20,25,30]
# c = list(map(lambda x,y : x+y , a,b))
# print(c)

# a =['sdsd','dfdf','fdfd']
# b = list(map(lambda x : x.upper(),a))
# print(b)

# a =['apple', 'banana', 'cherry', 'date']
# # find length of each word?
# b = list(map(lambda x : len(x) , a))
# print(b)

# a = ['apple', 'banana', 'cherry', 'date']

# b = list(map(lambda x,y :x+y ,[1,2,3],[2,3]))
# print(b)

# a = [1,2,3,4]
# b =[2,3,4,5]
# c = list(zip(a,b))
# print(c)

# Convert a zipped object into a dictionary.
# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# c ={ k : v for k ,v in zip(a,b)}
# print(c)

# Zip three lists together.
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# c = [True, False, True]
# zipped = list(zip(a, b, c))
# print(zipped)

# a = [1,2,3]
# b =['a','b']

# c = list(zip(a,b))
# print(c)

# a = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
# # Unzip the list of tuples.
# unzipped = list(zip(*a))
# print(unzipped)

# for i in unzipped:
#     print(list(i))

# a = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# # Unzip and assign
# nums, chars, flags = zip(*a)

# # Convert to lists if needed
# nums = list(nums)
# chars = list(chars)
# flags = list(flags)

# print(nums)
# print(chars)
# print(flags)

# a =[1,2,3,4]
# b =[2,3,4,5]
# c = list(zip(a,b))
# print(c)
# d = list(enumerate(a))
# print(d)

# Join a list of words into a sentence.
# a =['Python', 'is', 'best']
# sen = ' '.join(a)
# print(sen)
# print(' '.join('Python'))

# def gcd(a,b):
#     while b!=0:
#         a,b = b, b%a
#     return a
# m,n = map(int,input().split())
# print(gcd(m,n))
    

# 2. Sum of Digits of a Number

# n = int(input("Enter num : "))
# sum_digit = 0
# while n>0:
#     sum_digit += n%10
#     n = n//10
# print(sum_digit)

# def rev_string(s):
#     return s[::-1]
# print(rev_string('adfer'))

# import math 
# n = int(input("Enter Num :"))
# if n<=1:
#     print('Not Prime')
    
#     for i in range(2,math.sqrt()+1):
#         if n%i ==0:

# import math

# n = int(input())
# if n <= 1:
#     print("Not Prime")
# else:
#     is_prime = True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     print("Prime" if is_prime else "Not Prime")

# s = input().lower()
# vow = set("aeiou")

# count = sum(1 for char  in  s if char in vow)

# print(count)

# Sum of Digits of a Number

# a = int(input("Enter NUm :"))
# a = str(a)
# sum=0
# for char in a:
#     sum +=int(char)
# print(sum)

# a = int(input(("Enter NUm :")))
# sum =0
# while a!=0:
#     sum += a%10
#     a//=10
# print(sum)

# def sumOfDigits(n):
#     if n==0:
#         return 0
    
#     return n%10 +sumOfDigits(n//10)
# print(sumOfDigits(123))

# reverse the digit 

# a = 12345
# s=str(a)
# rev =s[::-1]
# rev_num = int(rev)
# print(rev_num)

# print(type(rev_num))

# n= 12345 
# rev =0
# while n>0:
#     a = n%10
#     rev = rev*10 + a
#     n//=10
    
# print(rev)    
    
# def isPrime(n):
#     if n<=1:
#         return False
    
#     for i in range(2,n):
#         if n%1==0:
#             return False
#     return True
    
# A school method based Python3
# program to check if a number
# is prime


# def isPrime(n):

#     # Corner case
#     if n <= 1:
#         return False

#     # Check from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# # Driver Program to test above function
# print("true") if isPrime(2) else print("false")
# print("true") if isPrime(14) else print("false")

# Digital Root (repeated digital sum) of the given large integer

# Check if a number is Palindrome

def is_palindrome(n):
    rev =0
    temp = n
    while n>0:
        a = n%10 
        rev = rev*10+a
        n //=10
    if rev == temp:
        print(f"{temp}, is palindrome")
    else :
        print("No")
is_palindrome(1234321)
