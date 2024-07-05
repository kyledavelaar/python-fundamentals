
def myFuncWithKeywordArgs(name, age):
    print("{} is {} years old".format(name, age))


# keyword args can come in any order as long as argument name matches parameter name
myFuncWithKeywordArgs(age=11, name="kyle")

# single * is for getting all the arguments (note args can be named anything could be myArgs)


def myFunc(*args):
    for x in args:
        print(x)


myFunc(1, 2, 3)


#  double star is for keywordArgs
def myFunc2(**kwArgs):
    print("the age arg is {}".format(kwArgs.get('age')))

    for x in kwArgs.values():
        print(x)

    for x in kwArgs.keys():
        print(x)


myFunc2(age=22, name='bill')


# *args must come before **kwArgs
def ordering(arg1, arg2, *args, **kwArgs):
    pass



def printArgs(**kwArgs):
    for arg in kwArgs:
        print(arg, kwArgs[arg])



input = { "a": 1, "b": 2 }

# can use ** to destructure dict and pass in as kwArgs
printArgs(**input)
# same as above
printArgs(a=input["a"], b=input["b"])

