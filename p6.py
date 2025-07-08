# Q6: Write a Python function to find the fourth largest number in a list
# without using built-in sort() or max() functions.
#
# Example:
# Input: [10, 40, 20, 5, 30, 25, 35]
# Output: 25

def fourth_largest(nums):
    first = second = third = fourth = float('-inf')

    for num in nums:
        if num > first:
            fourth = third
            third = second
            second = first
            first = num
        elif num > second and num != first:
            fourth = third
            third = second
            second = num
        elif num > third and num != second and num != first:
            fourth = third
            third = num
        elif num > fourth and num != third and num != second and num != first:
            fourth = num

    return fourth
nums = [10, 40, 20, 5, 30, 25, 35]
print("fourth largest number is:", fourth_largest(nums))
    