# Exercise 9: Find the Missing Number
# Implement a function that takes a list of integers from 1 to n with one number missing
# and returns the missing number.
def find_missing_number(nums: list[int]) -> int:
    for i,v in enumerate(nums):
        if v-1 != i:
            return i+1
    return -1
