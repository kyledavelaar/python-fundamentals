# partials allow us to bind certain arguments to a function

from functools import partial

def sayHi(name, greeting):
    return f"{greeting} {name}"

print(sayHi("kyle", "hello"))

# use kwargs if targeting arg other than the first arg
sayHiBoundInSpanish = partial(sayHi, greeting="hola")

print(sayHiBoundInSpanish("mario"))


def greet_friends(greeting, f1, f2, f3):
    return f'{greeting} {f1}, {f2}, {f3}'

# if targeting the first arg you don't need a kwarg
say_hi = partial(greet_friends, 'hi')
print(say_hi('charlie', 'marie', 'claire'))


