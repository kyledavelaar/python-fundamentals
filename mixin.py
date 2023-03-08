# Like an interface in Java
# sub class inherits from mixin class but child does not have the isA relationship to the mixin
# mixin is just a set of functions that you want a child class to have access to and could be passed to a number of classes that are all different (don't all have the same isA relationship)


class MathMixin:
    def __init__(self, result=0):
        self.result = result

    def add(self, x):
        self.result += x
        return self

    def subtract(self, x):
        self.result -= x
        return self

    def equals(self):
        return self.result


class Operator(MathMixin):
    def __init__(self, number):
        super().__init__(number)


operator = Operator(8)

print(operator.add(10).subtract(5).equals())
