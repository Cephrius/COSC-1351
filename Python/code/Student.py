
class Student:
    university = "HCU"
    def __init__(self,sid,sname):
        self.id = sid
        self.name = sname
        self.courses = []

    def add_courses(self,courses):
        self.courses.append(courses)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, sid):
        if (sid > 0 or sid < 10000):
            self._id = sid
        else:
            ("That's too big of an ID")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, sname):
        if (sname.isdigit()):
            print("Sorry the name cant be a digit..")
            self._name = "no Name"
        else:
            self._name = sname

    def __str__(self):
        return (f"Student {self.id} name is {self.name} is taking courses {self.courses} at University {self.university}")


s1 = Student(11,"Amy")
s2 = Student(2,"John")

s1.add_courses("COSC 1352")
s1.add_courses("ENSC 1411")

s2.add_courses("ENSC 1411")
s2.add_courses("COSC 1351")

Student.university = "Houston Baptist University"
print(str(s1))

