

#################################################################
# DECORATORS
#############################################################
def append_kyle(old_func):
    def append(*args, **kwargs):
        return old_func(*args, **kwargs) + 'kyle'
    return append


@append_kyle
def write(*args, **kwargs):
    return args[0] + " " + kwargs.get("name") + ' my name is '


print(write("yo", name="maria"))
print(write("hello", name="good sir"))


#################################################################
# Decorator that accepts an argument
#################################################################
def type_check(correct_type):
    def check(old_function):
        def dec_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                return "Bad Type"
        return dec_function
    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))



#################################################################
#
#################################################################
def double(old_function):
    def new_func(*args, **kwargs):
        sum = 0
        for i in range(2):
            sum += old_function(*args, **kwargs)
        return sum
    return new_func


@double
def mult(a, b):
    return a * b


print(mult(4, 5))

#################################################################
#
#################################################################



