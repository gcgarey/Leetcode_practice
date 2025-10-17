# Leetcode 238: Product of Array Except Self

def productExceptSelf(nums):
    preSum = 1
    newList = [1] * len(nums)
    for i in range(len(nums)):
        newList[i] = preSum
        preSum *= nums[i]

    postSum = 1
    for i in range(len(nums) - 1, -1, -1):
        newList[i] *= postSum
        postSum *= nums[i]
        
        
    return newList
        
print(productExceptSelf([1,2,3,4]))