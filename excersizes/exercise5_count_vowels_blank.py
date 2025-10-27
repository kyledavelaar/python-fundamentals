import re
# Exercise 5: Count Vowels in a String
# Implement a function that counts the number of vowels in a string.
def count_vowels(s: str) -> int:
    v = re.compile(r'[aeiou]', re.IGNORECASE)
    return len(re.findall(v, s))