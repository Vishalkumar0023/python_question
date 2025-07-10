# Q10: Write a Python function to find the first element in a list
# that does not repeat anywhere else in the list.
#
# Example:
# Input: [2, 3, 4, 2, 3, 5, 4, 6]
# Output: 5

def first_non_repeating(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
    for num in nums:
        if freq[num] == 1:
            return num 
    return None
nums = [2, 3, 4, 2, 3, 5, 4, 6]
print("First non-repeating element:", first_non_repeating(nums))             