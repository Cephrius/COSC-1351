class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self._color = "red"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value ):
        if value > 0:
            self._radius = value
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return f"Circle with a radius of {self.radius} and color {self.color}"
    
    def getInfo(self):
        return f"Circle with a radius of {self.radius} and color {self.color} has an area of {self.area()} and a circumference of {self.circumference()}"w


        
c1 = Circle(2,"Red")
print(c1)