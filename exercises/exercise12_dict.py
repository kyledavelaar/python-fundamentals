from collections import defaultdict
from typing import Any
from functools import reduce

# Create a function called get_value that takes two arguments: key and dict. The function should return the value of the key in the dictionary if it exists, or None if the key does not exist.
def get_default(d: dict, k: Any) -> Any | None:
    return d.get(k, None)

# Write a function called retrieve_values that takes two arguments: keys and dict. The function should return a list of values for the keys in the dictionary if they exist, or an empty list if any of the keys do not exist.
def retrieve_values(keys: list[str], d: dict) -> list:
    return [d[k] for k in keys if k in d]

#Write a function called add_key that takes two arguments: key and dict. The function should add a new key-value pair to the dictionary if it does not already exist, or update the value of an existing key if it does
def add_key(k: Any, v: Any, d: dict) -> dict:
    d.setdefault(k, v)
    return d

# Write a function called remove_key that takes two arguments: key and dict. The function should remove a key-value pair from the dictionary if it exists, or do nothing if the key does not exist.
def remove_key(k: Any, d: dict) -> dict:
    d.pop(k, 'not found')
    return d

# merge two dictionaries.  the second dictionary should overwrite any keys in the first if keys are the same between both dicts
def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}
    # d1.update(d2)
    # return d1

def merge_n_dicts(l: list[dict]) -> dict:
    return reduce(lambda acc, curr: {**acc, **curr}, l, {})

def flatten_lists(l: list[list]) -> list:
    return reduce(lambda acc, curr: [*acc, *curr], l, [])

