import re
# Exercise 2: Check for Palindrome
# Implement a function that checks if a string is a palindrome.
def is_palindrome(s: str) -> bool:
    # s = s.replace(' ', '').lower()
    s = re.sub(r'\s', '', s).lower()
    print(s)
    return s == s[::-1]