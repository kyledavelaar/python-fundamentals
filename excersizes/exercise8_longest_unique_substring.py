# Exercise 8: Find the Longest Substring Without Repeating Characters
def longest_unique_substring(s: str) -> int:
    seen = {}
    start = max_length = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length