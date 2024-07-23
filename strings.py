########## string formatting ####################
x = 10
y = 15
myString = "x is {} and y is {}"
print(myString.format(x, y))

# python 3.6 makes this easier with f-strings
f_string = f"x is {x} and y is {y}"
print(f_string)

############ string slicing ########################
st1 = "kyle"
print(st1[1:2]) # y
print(st1[:-1]) # kyl => go from 0 to last item
print(st1[:-2]) # ky => go from 0 to penultimate item
print(st1[-3:]) # yle

print("01/frame_00003_pose.txt"[:-7])

############ strings are immutable ############################
# strings are immutable so if need to change use "replace"
a = "hello my name is kyle"
b = a.replace("kyle", "billy")
print(a)
print(b)

############ escaping strings #########################################
# if don't want to have to escape every character can use "r" before string (r means "raw")
c = "my\file\path\for\windows" # here f is not the character f but \f which breaks the line
d = r"my\file\path\for\windows"
print(c)
print(d)


s = "Hello my name is"
t = s.find("o")
print(t) # 4

print(s.lower())
print(s.upper())







