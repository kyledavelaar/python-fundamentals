
# allows you to assign a value to a variable as part of an expression
# that you can then use later
# it reduced the amount of lines of code needed to write

while (text := input('say something: ')) != 'quit':
    print(f'you said: {text}')

# without := you would have to write it like this
# text = input('say something: ')
# while text != 'quit':
#     print(f'you said {text}')
#     text = input('say something: ')




# can use them in list comprehension to avoid repeated calculations
items = [[1,2], [3,4], [5]]
results = [length for item in items if (length := len(item)) > 1]
print('results: ', results)