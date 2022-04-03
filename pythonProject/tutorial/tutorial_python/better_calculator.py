num1 = float(input("Insert first number: "))
operator = input("Insert the operator: ")
num2 = float(input("Insert second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Please insert a valid operator")