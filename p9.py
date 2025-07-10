# Q9: Write a Python function to reverse a list manually
# without using reverse() method or slicing (like [::-1]).
#
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse_no(nums):
    reversed=[]
    for i in range(len(nums)-1,-1,-1):
        reversed.append(nums[i])
    return reversed 
nums = [1, 2, 3, 4, 5]
print("Reversed number",reverse_no(nums))
