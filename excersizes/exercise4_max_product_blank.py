# Exercise 4: Find the Maximum Product of Two Numbers
# Implement a function that finds the maximum product of two numbers in a list.
def max_product(nums: list[int]) -> int:
    if len(nums) < 2: return 0
    nums_sorted = sorted(nums)
    return max(nums_sorted[0] * nums_sorted[1], nums_sorted[-1] * nums_sorted[-2])