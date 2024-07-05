
# ternary
z = 100
r = 10 if z > 20 else 40
print(r)

x = 10

if x > 20:
    print("greater than 20")
elif x < 10:
    print("less than 10")
elif x < 0:
    pass # no op, nothing will happen
else:
    print("something else")
