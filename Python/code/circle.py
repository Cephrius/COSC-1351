class Shape(object):

    def __init__(self,bColour, fColour):
        self.borderColour = bColour
        self.fillColour = fColour

    @property
    def borderColour(self):
        return self._borderColour
    @property
    def fillColour(self):
        return self._fillColour

    @fillColour.setter
    def fillColour(self, fColour):
        self._fillColour = fColour

    @property
    def borderColour(self):
        return self._borderColour

    @borderColour.setter
    def borderColour(self,bColour):
        self._borderColour = bColour

class circle(Shape):

    def __init__(self, fColour, bColour, r =0):
        Shape.__init__(self, fColour, bColour)
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def __add__(self, anotherCircle):
        print(f"We are adding the {self.fillColour} circle and the {anotherCircle.colour} circle")
        return self.radius + anotherCircle.radius

    def __lt__(self, anotherCircle):
        if self.radius < anotherCircle.radius :
            print(f"{self.fillColour} is less than {anotherCircle.fillColour} ")
        else:
            print(f"{anotherCircle.fillColour} is less than {self.fillColour}")

##################################
#r1 = int(input("Enter the radius of the first circle: "))
#colour1 = input("Enter the colour of the first circle: ")

#r2 = int(input("Enter the radius of the second circle: "))
#colour2 = input("Enter the colour of the second circle: ")


c1 = circle("Blue","Green",5)
c2 = circle("Yellow","Orange",4)
c3 = circle("Brown", "Periwinkle",6)

c3 < c2
