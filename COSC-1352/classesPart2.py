
class Shape:
    def __init__(self, bColor, fColor):
        self.borderColor = bColor
        self.fillColor = fColor

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
    

class Square(Shape):
    def __init__(self, length):
        super().__init__(bColor,fColor)
        self.length = length
        self.area = length * length
        
    