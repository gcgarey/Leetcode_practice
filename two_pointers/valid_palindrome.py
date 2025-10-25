def valid_palindrome(s):
    res = ""
    for let in s:
        if let.isalnum():
            res += let
    return res == res[::-1]