# Q2: Find and print all even numbers in a list
# Example:
# Input: [1, 2, 3, 4, 5, 6]
# Output: 2, 4, 6

def find_even(nums):
    total=[]
    for num in nums:
        if num % 2 == 0:
            total.append(num)
    return total
nums = [1, 2, 3, 4, 5, 6]         
print("Even number of list",find_even(nums))