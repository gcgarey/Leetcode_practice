# Two Sum 2 - Input Array is Sorted

def twosumtwo(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        print(f" {l} {r}")
        num = numbers[l] + numbers[r]
        if num == target:
            return [l + 1, r + 1]
        elif num > target:
            r -= 1
        else:
            l += 1
print(twosumtwo([2,7,11,15], 9))