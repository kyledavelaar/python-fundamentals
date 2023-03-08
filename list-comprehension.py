

# a lot like map where first arg is a variable you use inside your logic
# faster way to return a list that had some calculations done to it


# Example 1
fruits = ['apple', 'pear']
# [expression, iterator, condition]
fruits_with_r = [fruit for fruit in fruits if "r" in fruit]
print(fruits_with_r)

# expression is current item but can change it too in the expression, and can omit filter at end to return all fruits capitalized
capitalized_fruit = [fruit.upper() for fruit in fruits]
print(capitalized_fruit)


# Example 2
sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split(' ')
word_lengths = [len(word) for word in words if word != 'the']
print(word_lengths)
