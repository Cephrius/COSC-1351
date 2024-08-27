#  create a students class that has the students name, id and courses

class Student:
    university = "HCU"
    def __init__(self,sid,sname):
        self.id = sid
        self.name = sname
        self.courses = []

    def add_courses(self,courses):
        self.courses.append(courses)

    def __str__(self):
        return (f"Student {self.id} name is {self.name} is taking courses {self.courses} at University {self.university}")
    