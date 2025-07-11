# Q14: Given a list where every number appears twice except one,
# write a Python function to find that unique number.
#
# Example:
# Input: [1, 2, 3, 2, 1]
# Output: 3

def find_unique_using_xor(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique 
nums = [1, 2, 3, 2, 1]
print("Unique no ",find_unique_using_xor(nums)) 