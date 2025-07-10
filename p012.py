# Q12: Write a Python function to find the missing number in a list
# containing numbers from 1 to n with one number missing.
#
# Example:
# Input: [1, 2, 4, 5, 6] → n = 6
# Output: 3

def find_missing_no(nums):
    expected_sum = 0
    for i in range(1, len(nums) + 2):
        expected_sum += i
    actual_sum = 0
    for num in nums:
        actual_sum += num 
    return expected_sum - actual_sum
nums = [1, 2, 4, 5, 6]
print("Missing number in list",find_missing_no(nums))     

