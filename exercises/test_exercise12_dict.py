import pytest
from exercise12_dict import *

def test_get_default():
    assert get_default({"a": 1 }, "a") == 1
    assert get_default({"a": 1 }, "b") == None

def test_retrieve_values():
    assert retrieve_values(['a', 'c'], {"a": 10, "b": 20, "c": 30}) == [10, 30]
    assert retrieve_values(['e', 'f'], {"a": 10, "b": 20, "c": 30}) == []

def test_add_key():
    assert add_key('a', 1, {}) == {'a': 1}
    assert add_key('a', 1, {'a': 1}) == {'a': 1}
    assert add_key('a', 2, {'a': 1}) == {'a': 1}

def test_remove_key():
    assert remove_key('a', {'a': 1, 'b': 2}) == {'b': 2}
    assert remove_key('c', {'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

def test_merge_dicts():
    d1 = {'d': 1, 'c': 4}
    d2 = {'a': 3, 'b': 2}
    res = {'a':3, 'b':2, 'c':4, 'd':1}
    assert merge_dicts(d1, d2) == res
    res['a'] = 9
    print(id(res['a']))
    print(id(d2['a']))
    assert d2['a'] == 9
    assert merge_dicts({}, {'b': 2}) == {'b':2}
    assert merge_dicts({'b': 2}, {}) == {'b':2}

def test_merge_n_dicts():
    assert merge_n_dicts([{'a': 1, 'c': 4}, {'a': 3, 'b': 2}]) == {'a':3, 'b':2, 'c': 4}
    assert merge_n_dicts([{'a': 1}, {'b': 2}, {'c': 3}]) == {'a':1, 'b':2, 'c': 3}
    assert merge_n_dicts([{'a': 1}]) == {'a':1}
    assert merge_n_dicts([]) == {}

def test_flatten_lists():
    assert flatten_lists([[1,2],[3,4]]) == [1,2,3,4]
    assert flatten_lists([[1],[3],[5]]) == [1,3,5]
    assert flatten_lists([[1]]) == [1]
    assert flatten_lists([[]]) == []