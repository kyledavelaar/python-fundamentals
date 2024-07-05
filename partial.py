# partials allow us to bind certain arguments to a function

from functools import partial

def sayHi(name, greeting):
    return f"{greeting} {name}"

print(sayHi("kyle", "hello"))

sayHiBoundInSpanish = partial(sayHi, greeting="hola")

print(sayHiBoundInSpanish("mario"))






