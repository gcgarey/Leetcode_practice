# Leetcode 271: Encode and Decode Strings

def encode(strs: list[str]) -> str:
    newString = ""
    for word in strs:
        newString += str(len(word)) + "#" + word
    return newString
        
        
def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i : j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res
