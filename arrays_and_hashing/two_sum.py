# Leetcode 1: twoSum

def two_sum(nums, target):
    diff = {}
    for i in range(len(nums)):
        if target - nums[i] in diff:
            return i, diff[target - nums[i]]
        
        diff[nums[i]] = i
        
    return 0
