is_male = False
is_tall = True


# if is_male and is_tall:
#     print("You are male and tall")
# elif not is_male and is_tall:
#     print("You are not male but tall")
# elif is_male and not is_tall:
#     print("You are male but not tall")
# else:
#     print("You are not either male or tall")

def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_number(6, 5, 4))
