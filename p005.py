# Q6: Write a Python function to find the third largest number in a list
# without using built-in sort() or max() functions.
#
# Example:
# Input: [10, 40, 20, 5, 30]
# Output: 20
def third_max(nums):
    first_max = second_max = third_max = float('-inf')
    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            third_max = second_max
            second_max = num
        elif num > third_max and num != second_max and num != first_max :
            third_max= num
    return third_max
nums = [10, 40, 20, 5, 30]           
print("third largest number is:", third_max(nums)) 