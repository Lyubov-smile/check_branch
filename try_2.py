def getValue():
    x = input("x: ")
    y = input("y: ")

    try:
        x = int(x)
        y = int(y)
        return x, y
    except ZeroDivisionError as z:
        print(z)
        return 0, 0
    except ValueError as v:
        print(v)
        return 0, 0
    finally:
        print("finally run before return")


x, y = getValue()
print(x, y)

