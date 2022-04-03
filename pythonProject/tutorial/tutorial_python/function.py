def power_number(base_num, pow_num):
    result = 1

    for index in range(pow_num):
        result = result * base_num

    return result


print(power_number(6, 3))
