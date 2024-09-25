class Student(object):
    university = "HBU"
    
    def __init__(self,sid,sname):
        self.id = sid
        self.name = sname
        self.courses = []
    
    def addCourse(self,course):
        self.courses.append(course)
    
    def __str__(self):
        return "ID: " + str(self.id) + " Name: " + self.name
    
    # def get_id(self):
    #     return self.id
    
    # def set_id(self, sid):
    #     if(sid > 0 and sid < 100000):
    #         self.id = sid
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, sid):
        if(sid > 0 and sid < 100000):
            self._id = sid
    
    
s1 = Student(1234,"John")
print(s1)