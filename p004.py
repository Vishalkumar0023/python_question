# Q4: Find the second largest number in a list without using built-in sort() or max() functions.
# Example:
# Input: [10, 40, 20, 5, 30]
# Output: 30

def find_second_max(nums):
    first_max = float('-inf')
    second_max = float('-inf')
    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    return second_max
nums = [10, 40, 20, 5, 30] 
print("Second largest number is:", find_second_max(nums)) 
nums = [-5, -2, -10]        
print("Second largest number is:", find_second_max(nums))  

