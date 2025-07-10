# Q7: Write a Python function to count the frequency of each element in a list.
# Use a dictionary to store how many times each element appears.
#
# Example:
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}

def count_frequency(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

nums = [1, 2, 2, 3, 1, 4, 2]
print("Frequency of each element:", count_frequency(nums))
