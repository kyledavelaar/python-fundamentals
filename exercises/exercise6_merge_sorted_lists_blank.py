# Exercise 6: Merge Two Sorted Lists
# Implement a function that merges two sorted lists into one sorted list.
def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    l3 = list1 + list2
    # return sorted(l3)
    s = set(l3)
    return list(s)