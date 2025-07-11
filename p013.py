# Q13: Write a Python function to find all missing numbers
# in a list that should contain numbers from 1 to n.
#
# Example:
# Input: [1, 2, 4, 6]
# Output: [3, 5]

def find_missing_no(nums):
    missing =[]
    max_val = max(nums)
    for i in range(1,max_val +1):
        if i not in nums:
            missing.append(i)

    return missing
nums = [1, 2, 4, 6]    
print("Missing number ",find_missing_no(nums)) 