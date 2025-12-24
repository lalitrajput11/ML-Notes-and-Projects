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

s = 'applekwe'

l1 = [char for char in s if char in "aeiouAEIOU"]
print(l1)
