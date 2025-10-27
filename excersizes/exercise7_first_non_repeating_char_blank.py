# Exercise 7: Find the First Non-Repeating Character
# Implement a function that returns the first non-repeating character in a string.
# If all characters repeat, return an empty string.
def first_non_repeating_char(s: str) -> str:
    if len(s) == 0: return ''
    if len(s) == 1: return s
    l = [c for c in s]
    for i in range(0, len(l)-1, 2):
        if l[i+1] != l[i]:
            return l[i+1]
    return ''