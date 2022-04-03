try:
    value = 10 / 0
    print(int(input("Enter a number: ")))
except ZeroDivisionError as err:
    print(err)
except ValueError as err2:
    print(err2)
