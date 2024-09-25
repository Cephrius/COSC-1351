class Rectangle():
    def __init__(self, width, length) -> None:  # <----- Called magic function because it is automatically invoked
        self.length = length
        self.width = width
        self.area = length * width

    def calcluateArea(self):
        return (f"The area of the rectangele is {self.area}")
    
    def __str__(self) -> str:
        return(f"This Rectangle has a length of {self.length} and a width of {self.width} ")
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        self._length = value
    
    

r1 = Rectangle(10, 20)

print(r1)
print(r1.calcluateArea())
print(r1.width)
r1.length = 30
print(r1.length)