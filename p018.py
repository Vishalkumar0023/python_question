# Q18: Write a Python function to find the first repeating element in a list.
# The function should return the first element that repeats (appears more than once)
# and whose second occurrence has the smallest index.
#
# Example:
# Input: [1, 5, 3, 4, 3, 5, 6]
# Output: 5

def first_repeating_element(nums):
    index_map = {}
    first_repeat_index = len(nums)
    answer = None

    for i, num in enumerate(nums):
        if num in index_map:
            if index_map[num] < first_repeat_index:
                first_repeat_index = index_map[num]
                answer = num
        else:
            index_map[num] = i

    return answer

nums = [1, 5, 3, 4, 3, 5, 6]
print("First repeating element:", first_repeating_element(nums))
