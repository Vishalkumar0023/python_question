# Q16: Write a Python function to find all unique pairs in the list
# that sum up to a given target number.
#
# Example:
# Input: [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]

def find_pairs(nums,target):
    pairs = []
    n =len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs
target = 7
nums = [2, 4, 3, 5, 7]
print("Pairs with sum", target, ":", find_pairs(nums, target))
