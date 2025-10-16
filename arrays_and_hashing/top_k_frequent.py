# Leetcode 347: top k frequent elements
from collections import defaultdict
def top_k_frequent(nums, k):
    counter = defaultdict(int)
    res = []

    for num in nums:
        counter[num] += 1
    print(counter)
    counter = sorted(counter.items(), key=lambda x:x[1])
    print(counter)

    for i in range(len(counter) - 1, -1, -1):
        res.append(counter[i][0])
        if len(res) == k:
            return res

print(top_k_frequent([1,1,1,2,2,3, 3, 3, 3, 3], 2))
