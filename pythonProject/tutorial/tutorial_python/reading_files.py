employee_file = open("Names.txt", "r")

for line in employee_file.readlines():
    print(line)
# print(employee_file.read())
employee_file.close()
