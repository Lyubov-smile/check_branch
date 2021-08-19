def getValue():
    x = input("x: ")
    y = input("y: ")

    try:
        x = int(x)
        y = int(y)
        return x, y, x/y
    except ZeroDivisionError as z:
        print(z)
        return 0, 0, 0
    except ValueError as v:
        print(v)
        return 0, 0, 0
    except:
        print("Another exception")
    finally:
        print("finally run before return")


x, y, res = getValue()
print(x, y, res)

