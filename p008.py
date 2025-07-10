# Q8: Write a Python function that returns all the unique elements from a list.
# An element is considered unique if it appears exactly once in the list.
#
# Example:
# Input: [1, 2, 2, 3, 1, 4, 5]
# Output: [3, 4, 5]

def find_unique(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    uniques = []
    for num in freq:
        if freq[num] == 1:
            uniques.append(num)

    return uniques

nums = [1, 2, 2, 3, 1, 4, 5]
print("Unique elements are:", find_unique(nums))