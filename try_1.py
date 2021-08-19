x = input("x: ")
y = input("y: ")

try:
    x = int(x)
    y = int(y)

    res = x/y
except ZeroDivisionError as z:
    res = z
except ValueError as v:
    res = v
else:
    res = "no exceptions happened"

print(res)
