from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef

student1 = Student("Jim", "CSE", 3, False)
student2 = Student("Kim", "EEE", 3.5, False)
# print(student2.on_honor_role())

myChef = Chef()
myChef.make_special_dish()
myChef.make_chicken()
myChef.make_salad()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_Rice_bowl()