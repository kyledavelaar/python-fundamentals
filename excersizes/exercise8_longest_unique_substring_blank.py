# Exercise 8: Find the Longest Substring Without Repeating Characters
# Implement a function that returns the length of the longest substring without repeating characters.
def longest_unique_substring(s: str) -> int:
    longest = 0

    for i in range(0, len(s)-1):
        length = 1
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                length += 1
            else:
                if longest < length:
                    longest = length
                break

    return longest
