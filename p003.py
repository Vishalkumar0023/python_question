# Q3: Count how many odd numbers are present in a list
# Example:
# Input: [1, 2, 3, 4, 5, 6]
# Output: 3

def find_odd_no(nums):
    odd_num=0
    for num in nums:
        if num % 2 != 0:
            odd_num += 1
    return odd_num 
nums = [1, 2, 3, 4, 5, 6] 
print("Odd number count",find_odd_no(nums))    