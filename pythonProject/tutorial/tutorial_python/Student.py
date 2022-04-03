class Student:

    def __init__(self, name, major, gpa, is_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_probation = is_probation

    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
