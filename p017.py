# Q16: Write a Python function to find the most frequent element in a list.
#
# Example:
# Input: [1, 3, 2, 1, 4, 1, 3]
# Output: 1
def most_frequent_element(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = 0
    most_frequent_num = None
    for num in freq:
        if freq[num] > max_freq:
            max_freq = freq[num]
            most_frequent_num = num
    return most_frequent_num

nums = [1, 3, 2, 1, 4, 1, 3]
print("Most frequent element : ",most_frequent_element(nums))

