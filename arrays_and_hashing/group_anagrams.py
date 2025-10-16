# Leetcode 49: Group Anagrams

def group_anagrams(strs):
    # hashmap [list of letters -> list of words]
    unique = {}
    # loop through strs
    for word in strs:
        # create a list of 26 0s that I fill up with letters
        new = [0] * 26
        for let in word.lower():
            new[ord('a') - ord(let)] += 1
        # check that against hashmap and add if needed
        if tuple(new) in unique:
            unique[tuple(new)].append(word)
        else:
            unique[tuple(new)] = [word]

    # return the values as one list
    return list(unique.values())

