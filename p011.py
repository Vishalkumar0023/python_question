# Q11: Write a Python function to find all elements in a list
# that appear more than once (duplicates).
#
# Example:
# Input: [1, 2, 3, 2, 4, 5, 1, 6, 3]
# Output: [1, 2, 3]

def repeating_no(nums):
    freq = {}
    repeating_no = []
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
    for num in freq:
        if freq[num] > 1:
            repeating_no.append(num)
    return repeating_no           
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
print("Repeating element:", repeating_no(nums))    