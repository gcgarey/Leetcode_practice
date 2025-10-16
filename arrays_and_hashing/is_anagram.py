# Leetcode 242: Valid Anagram 

from collections import defaultdict 

def isAnagram(s, t):
    s_char = defaultdict(int)
    t_char = defaultdict(int)
    for let in s:
        s_char[let] += 1

    for let in t:
        t_char[let] += 1

    return s_char == t_char

print(isAnagram("ray", "tar"))