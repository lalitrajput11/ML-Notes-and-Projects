'''https://www.ccbp.in/blog/articles/python-coding-questions'''

# def armstrong_num(num):
#     str_num= str(num)
#     len_num = len(str(num))
#     sum = 0
#     for digit in str_num:
#         sum += int(digit)**len_num
#     if sum == num:
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")
# armstrong_num(153)

# def check_perfect(n):
#     sum =0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     if n ==sum :
#         print(f"The number {n} is Perfect Number")
#     else:
#         print(f"The number {n} is not perfect number")
# check_perfect(28)


# def check_even_odd(n):
#     [print("Even") if n%2==0 else print("Odd")]
# check_even_odd(7)

# def multiplication_table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} =",n*i)
# multiplication_table(5)

# def summ_of_naturals(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
    
# def add_num(n):
#     print(n*(n+1)/2)
    
# summ_of_naturals(5)
# # add_num(5)

# def sum_of_squares(n):
#     sum = (n*(n+1)*(2*n+1))/6
#     print(sum)
# sum_of_squares(4)

# def sum_of_squares(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i*i
#     print(sum)
# sum_of_squares(4)

# def swap_num(a,b):
#     temp =a
#     a=b
#     b=temp
#     print(a,b)
 
 
# def swap_num1(a,b):   
#     a,b =b,a
#     print(a,b)
    
# swap_num1(3,5)

# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

# Examples: 

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the closest to 13, divisible by 4.

# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.

# def closest_num(n,m):
#     closest = 0
#     min_diff = float('inf')
    
#     for i in range(n-abs(m),n+abs(m)+1):
#         if i%m==0:
#             diff = abs(n-i)
#             if diff < min_diff or diff==min_diff and abs(i)>abs(closest):
#                 min_diff = diff
#                 closest = i
#     return closest
# print(closest_num(-15,6))
      
# def opp_dice(m):
#     return 7-m

# print(opp_dice(3))

# def opp_of_dice(m):
#     if m==1:
#         return 6
#     elif m==2:
#         return 5
#     elif m==3:
#         return 4
#     elif m==4:
#         return 3
#     elif m==5:
#         return 2
#     else:
#         return 1
    
# print(opp_of_dice(2))

# Input : a1 = 2,  a2 = 3,  n = 4
# Output : 5
# Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

# Input : a1 = 1, a2 = 3, n = 10
# Output : 19
# Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.

# def ap_Nth_Term(a1,a2,n):

#     d = a2-a1
#     nth_term = a1 + (n-1)*d
#     return nth_term

# print(ap_Nth_Term(2,3,4))  #5
# print(ap_Nth_Term(1,3,10)) #19

# def nth_term(a1,a2,n):
#     d = a2-a1
#     nth_num=a1
#     for i in range(1,n):
#         nth_num+=d
        
#     return nth_num

# print(nth_term(2,3,4))  #5

# def sum_of_digits(n):
#     sum=0
#     for i in str(n):
#         sum+=int(i)
#     return sum

# print(sum_of_digits(1234))

# def sum_of_digits(num):
#     sum=0
#     while num>0:
#          sum +=num%10
#          num=num//10
#          print(num)
         
#     return sum 
# print(sum_of_digits(1234))

# print(1//10)

# def reverse_digits(n):
#     rev=0
#     while n>0:
#         rev= rev*10+n%10
#         n = n//10
#     return rev
# print(reverse_digits(1234))

# def prime_num(n):
#     count =0
#     for i in range(2,n):
#         if n%i==0:
#             count+=1
#     if count==0:
#         print("num is prime")
#     else:
#         print("NUm is notprime")
        
# prime_num(6)

# def prime_num(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
        
#     return True

# print(prime_num(4))
        
# def check_if_num_is_power2anotherNUm(a,b):
#     if a**2 ==b or b**2==a:
#         print("isPower")
        
#     else:
#         print("No")
# check_if_num_is_power2anotherNUm(10,100)

# import math
# def distance(x1,y1,x2,y2):
#     dis =math.sqrt((x2-x1)**2+(y2-y1)**2)
#     print(dis)
    
# distance(2,1,3,4)

# import math
# def distance(x1,x2,y1,y2):
#     return math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))

# print(distance(2,3,4,5))

# def valid_triangle(a,b,c):
#     if a+b>c or a+c>b or b+c>a:
#         print(" Valid")
#     else:
#         print("NOt valid traingle")
        
# valid_triangle(2,3,4)

# def fact(n):
#     facto =1
#     for i in range(1,n+1):
#         facto*=i
#     print(facto)
    
# fact(5)



# def gcd(a,b):
#     while b:
#         a,b = b, a%b
#     return a
# print(gcd(24,36))

# print(36%24)

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(36,22))


# def gcd(a,b):
#     while b:
#         a,b =b,a%b
#     return a
# print(gcd(24,36))

# import math
# def gcd(a,b):
#     return math.gcd(a,b)    

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(a-b,b)
# print(gcd(36,24))

# def gcd(a,b):
#     return a if b ==0 else gcd(b,a%b)

# def lcm(a,b):
#     return (a*b)//gcd(a,b)
# print(lcm(4,6))

# def lcm(a,b):
#     max =a if a>b else b
#     min=b if b<a else a
    
#     for i in range(max,a*b+1,max):
#         if i%min==0:
#             return i
#     return a*b

# print(lcm(2,3))


# def lcm(a,b):
#     max_num =max(a,b)
#     min_num = min(a,b)
    
#     for i in range(max_num,a*b+1,max_num):
#         if i%min_num==0:
#             return i
        
#     return a*b

# print(lcm(48,94))

# import math

# def lcm(a,b):
#     return abs(a*b)//math.gcd(a,b)

# print(lcm(4,6))

# def is_perfect_num(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     if sum == n:
#         return True
#     return False
    
# print(is_perfect_num(15))

#Program to add fractions
# a =[2,3]
# b=[4,5]

# num = (a[0]*b[1] + a[1]*b[0])
# den = a[1]*b[1]

# print(f"Freaction's Sum : {num}/{den} = {num/den}")


# def nth_finonacci(n):
#     if n<=1:
#         return n
#     return nth_finonacci(n-1)+nth_finonacci(n-2)

# print(nth_finonacci(5))

# '''Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.'''

# def contains_duplicate(nums):
#     return len(nums) !=len(set(nums))
# nums =[1,2,3,1]
# print(contains_duplicate(nums))

# def contains_duplicate(nums):
#     for n in nums:
#         if nums.count(n)>1:
#             return True
#     return False
# nums =[1,2,3,1]
# print(contains_duplicate(nums))

# def contains_duplicate(nums):
#     for n in nums:
#         count=0
#         for m in nums:
#             if n==m:
#                 count+=1
#         if count>1:
#             return True
#     return False
# nums =[1,2,3,1]
# print(contains_duplicate(nums)) 

# def contains_duplicate(nums):
#     nums.sort()
#     for i in range(1,len(nums)):
#         if nums[i]==nums[i-1]:
#             return True
#     return False
# nums =[1,2,3,1]
# print(contains_duplicate(nums))

# def contains_duplicate(nums):
#     seen=set()
#     for n in nums:
#         if n in seen:
#             return True
#         seen.add(n)
#     return False
# nums =[1,2,3,1]
# print(contains_duplicate(nums)) 

# def contains_duplicate(nums):
#     seen ={}
#     for n in nums:
#         if n in seen:
#             return True
#         seen[n]=1
#     return False
# nums =[1,2,3,1]
# print(contains_duplicate(nums))



###############################################################

# check Anagrams:
# def are_anagrams(str1,str2):
#     if sorted(str1) == sorted(str2):
#         return True
#     return False

# print(are_anagrams("listen","silent"))  #True
# print(are_anagrams("hello","world"))    #False

def are_anagrams(str1,str2):
    for char in str1:
        if char not in str2:
            return False
        str2 = str2.replace(char,"",1)
        print(str2)
    return len(str2)==0
# print(are_anagrams("listen","silent"))  #True
print(are_anagrams("hello","world"))    #False