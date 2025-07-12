#Q14: Write a Python function to find all missing numbers
# in a list that should contain numbers from 1 to n.
# With sorted() and set() function.
# Example:
# Input: [1, 2, 4, 6]
# Output: [3, 5]

def find_all_missing(nums):
    max_val = max(nums)
    full_set = set(range(1, max_val + 1))
    actual_set = set(nums)
    missing = full_set - actual_set
    return sorted(list(missing))

nums = [1, 2, 4, 6]
print("Missing numbers are:", find_all_missing(nums))
