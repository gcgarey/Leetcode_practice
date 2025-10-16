# Leetcode 217 - Contains Duplicate

def contains_duplicate(nums):
    seen = set(nums)
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 4, 1]))

