# Exercise 4: Find the Maximum Product of Two Numbers
def max_product(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])