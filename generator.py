


# yield keyword makes something a generator
# generator will not be called when use ()
# instead it will only be called when you use it later
# generators use less memory b/c they don't have to hold entire list in memory like for loops do
# they can do this b/c they only process one item at a time like a stream

def squares(n=10):
    for num in range(1, n+1):
        yield num **2

squares_g = squares(5)
print(squares_g)


for n in squares_g:
    print(n)



########## generator expressions ###############
print('__________generator expressions______')
# same as list comprehensions but with () instead
gen = (x**2 for x in [1,2,3] if x > 1)

for n in gen:
    print(n)



########## iter tools ###############
print('__________iter tools______')

import itertools

def first_letter(s):
    return s[0]

names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

# only groups consecutive elements, not all in entire list.  so Albert will be in separate group unfortunately
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))







