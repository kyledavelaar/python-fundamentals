from functools import partial
# Exercise 3: FizzBuzz
# Implement a function that returns a list of strings representing the numbers from 1 to n.
# For multiples of 3, return "Fizz"; for multiples of 5, return "Buzz"; for multiples of both, return "FizzBuzz".
def fizz_buzz(n: int) -> list[str]:
    return [get_word(i) for i in range(1, n+1)]

def is_mult(n: int, mult: int) -> bool:
    return n % mult == 0

is_mult_3 = partial(is_mult, mult=3)
is_mult_5 = partial(is_mult, mult=5)

def get_word(i: int) -> str:
    res = ''
    if is_mult_3(i):
        res += 'Fizz'
    if is_mult_5(i):
        res += 'Buzz'
    if res == '':
        res += str(i)
    return res