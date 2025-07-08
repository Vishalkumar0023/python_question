# Q1: Find the maximum number in a list (without using the built-in max() function)
# Example:
# Input: [10, 5, 30, 8, 20]
# Output: 30

def find_max(nums):
    max_num=nums[0]
    for num in nums:
        if num > max_num:
            max_num=num
    return max_num
nums = [10, 5, 30, 8, 20]
print("Maximum number:", find_max(nums))        


