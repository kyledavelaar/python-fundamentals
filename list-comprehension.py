
# Example 1

# [f(x) for x in items if condition]

nums = [1,2,3]
squared = [x**2 for x in nums if x > 2]
print(squared)



# Example 2
# f(x) here just returns x
fruits = ['apple', 'pear']
# [expression, iterator, condition]
fruits_with_r = [fruit for fruit in fruits if "r" in fruit]
print(fruits_with_r)

# Example 3
# expression is current item but can change it too in the expression, and can omit filter at end to return all fruits capitalized
capitalized_fruit = [fruit.upper() for fruit in fruits]
print(capitalized_fruit, "\n")


# Example 4
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(' ')
word_lengths = [len(word) for word in words if word != 'the']
print(word_lengths, "\n")


# can also do it on tier 2 lists
# here we flatten the tier-2 list into a tier-1
nums = [(1,2,3), (4,5,6)]
flat = [n for tup in nums for n in tup]
print(flat)














