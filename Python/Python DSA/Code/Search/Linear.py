# def linear_search(arr, target):
#     """
#     Perform a linear search on the given array to find the target value.

#     Parameters:
#     arr (list): The list to search through.
#     target: The value to search for.

#     Returns:
#     int: The index of the target if found, otherwise -1.
#     """
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#     return -1

# # Example usage:
# if __name__ == "__main__":
#     sample_array = [10, 23, 45, 70, 11, 15]
#     target_value = 70
#     result = linear_search(sample_array, target_value)
#     if result != -1:
#         print(f"Element found at index: {result}")
#     else:
#         print("Element not found in the array.")
        
class Fraction:
    def __init__(self,n,d):
        self.num =n
        self.den =d
    
    def __str__(self):
        return "{}/{}".format(self.num ,self.den)
    
    def __add__(self,other):
        temp_num = self.num*other.den + self.den*other.num
        temp_den = self.num*self.den
        
        return "{}/{}".format(temp_num,temp_den)
    
# x= fraction(2,3)
# print(x)
# y=fraction(4,3)
# print(y)
# print(x+y)