'''Check Even or Odd
1.[Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space

2.[Efficient Approach] Using Bitwise AND Operator - O(1) Time and O(1) Space'''

'''# Naive Approach
def is_even(n):
    if n%2 ==0:
        return True
    else:
        return False
# Efficient Approach

def is_even_bitwise(n):
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    number = 42
    if is_even(number):
        print(f"{number} is Even (Naive Approach)")
    else:
        print(f"{number} is Odd (Naive Approach)")

    if is_even_bitwise(number):
        print(f"{number} is Even (Bitwise Approach)")
    else:
        print(f"{number} is Odd (Bitwise Approach)")'''
        
#######################################################################

'''Program for multiplication table'''

'''def PrintTable(n):
    for i in range(1,11):
        print("%d * %d = %d" %(n ,i,n*i))
        
if __name__ == "__main__":
    num = 5
    PrintTable(num)'''
    
#######################################################################
    
'''Program for sum of n natural numbers'''

'''def SumNaturalNumbers(n):
    sum =0
    for i in range(1,n+1):
        sum+=i
    return sum
print(SumNaturalNumbers(5))
'''
'''[Expected Approach] Formula Based Method- O(1) Time and O(1) Space '''

'''def findsum(n):
    return n*(n+1)//2
print(findsum(5))'''

'''[Alternative Approach] Using Recursion -O(n) and O(n) Space'''
'''def fin_sum(n):
    if n==1:
        return 1
    else:
        return n + fin_sum(n-1)

print(fin_sum(5))'''

'''Swapping of Numbers'''

'''def swap(a,b):
    print(f"a : {a},b : {b} ")
    a = a+b
    b= a-b
    a=a-b
    return b,a

swap(2,5)'''

'''def SWAp(a,b):
    temp =a
    a = b
    b = temp
    
    print(a,b)
SWAp(5,6)'''

'''[Alternate Approach] Built-in Swap'''
'''a,b =3,5
a,b = b,a   # tuple umpacking
print(a,b)'''

##########################################################################

"Sum of square of natural numbers"

'''def sum_of_squares(n):
    return sum([i**2 for i in range(n+1)])

print(sum_of_squares(3))'''

'''def sum_of_squares(n):
    return n*(n+1)*(2*n+1)//6

print(sum_of_squares(3))'''

##############################################################################

# a = 12345
# b = str(a)

# sum =0
# for digit in b:
#     sum += int(digit)
# print(sum)

# def sumOFdigits(n):
#     if n==0:
#         return 0
#     return n%10 + sumOFdigits(n//10)
# print(sumOFdigits(12345))

# def reverseString(n):
#     s = str(n)
#     s = list(s)
    
#     s.reverse()
#     print(s)
    
#     s=''.join(s)
    
    
#     return s
# print(reverseString("abcd"))

# def countPairs(n):
#     count =0
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             if a**3+ b**3 == n : 
#                 count+=1
#     return count

from ex1 import fraction 

