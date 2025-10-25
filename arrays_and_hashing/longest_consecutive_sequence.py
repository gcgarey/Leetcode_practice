def longestConsecutive(nums) -> int:
    nums = set(nums)
    max_length = 0
    for num in nums:
        if num - 1 not in nums:
            temp = 1
            curr = num
            while curr + 1 in nums:
                temp += 1
                curr += 1
            max_length = max(max_length, temp)
    return max_length

print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4