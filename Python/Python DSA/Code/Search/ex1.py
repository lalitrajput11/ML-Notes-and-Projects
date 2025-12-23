word = input("Enter a word: ").strip()
count = int(input("How many times to repeat it? "))

# Create the repeated string with commas
result = (word + ", ") * (count - 1) + word   # adds comma after all except the last one

print("\nResult:")
print(result)