# descriptors extend the power of property decorators by creating re-usable code that may be used in multiple classes

# descriptor class (always implements these methods)
class RequiredString:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'The {self.property_name} must be a string')

        if len(value) == 0:
            raise ValueError(f'The {self.property_name} cannot be empty')

        instance.__dict__[self.property_name] = value


class Person:
    # property decorators call get_first_name/set_first_name/delete_first_name functions.
    # you can add your own set_first_name function for example to implement value checking
    first_name = RequiredString()
    last_name = RequiredString()

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name  # Validated by RequiredString
        self.last_name = last_name    # Validated by RequiredString
        self.age = age                # Validated by the age setter

    def __repr__(self):
        return f'Person:\nfirst_name: {self.first_name},\nlast_name: {self.last_name},\nage: {self.age},\nnetWorth: {self.netWorth}'

    @property
    def age(self):
        return self._age

    # if didn't use descriptor, this is how you could do setter checking
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("must be greater than 0")
        self._age = value

    # if want a property to be ReadOnly, don't create a setter method
    @property
    def netWorth(self):
        return 100


try:
    person = Person('kyle', 'davelaar', 30)
    print(person)
    # person.last_name = ''
    # person.age = 0
    # person.netWorth = 10 # this will throw an error b/c can't set netWorth
except Exception as e:
    print('Error: ', e)


