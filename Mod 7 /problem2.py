'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
'''




def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Racecar"))
print(is_palindrome("Radar"))
print(is_palindrome("castle"))
