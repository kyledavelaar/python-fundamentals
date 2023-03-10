class Person:
    # init is not a constructor b/c it doesn't create an object but "like" a constructor b/c holds similar logic that is in other languages' constructors
    def __init__(self, name="kyle", age=44):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi I am {self.name}"

    # shared by all instances of the class (good for performance) and not bound to an instance of this class
    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)


class Employee(Person):
    employeeCount = 0  # class Attribute and will be shared among all instances of this class

    def __init__(self, name, age, position="engineer", salary=0):
        super().__init__(name, age)
        self.position = position
        self.__salary = salary  # python doesn't have private variables but if you put __ before variable you can't do employee.__salary and get back result.  However you can do employee._Employee.__salary so it is not really private
        Employee.employeeCount += 1

    # can override default methods
    def __str__(self):
        return f'Person({self.name}, {self.age}, {self.position})'

    def getPosition(self):
        return "the position is " + self.position

    def getSalary(self):
        return self._Employee__salary

    # static methods can't access or alter the class state
    @staticmethod
    def getPersonType():
        return "Employee"


#########################################################################################################
person = Person()
print(person.greet())

# Use built in double under methods
print(Person.__name__)  # Person
print(person.__dict__)  # {'name': 'kyle', 'age': 44}

anon = Person.create_anonymous()
print(anon.name)
# getattr like _.get()
print("Get Attr getting age: " + str(getattr(anon, 'age', 99)))
print(Employee.getPersonType())

employee1 = Employee("Gus", 21, "Janitor", 800)
print(employee1)  # overrode __str__ method
print(employee1.getPosition())
print(employee1._Employee__salary)  # not really private
print(Employee.employeeCount)



