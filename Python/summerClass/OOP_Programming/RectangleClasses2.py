class Rectangle(object):
    def __init__(self, length, width) -> None: # <--- The constuctor
        self._length = length # <--- Initialize private variables
        self._width = width
        self._area = length * width
        
    @property
    def length(self):
       return self._length
   
    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
            self.area = length * self._width
        else:
            raise ValueError("Length must be greater than 0")
   
   
    @property
    def width(self):
       return self._width
   
    @width.setter
    def width(self, width):
       if width > 0: 
           self._width = width
           self.area = self._length * width
       else:
           raise ValueError("Width must be greater than 0")
   
    def __add__(self,other):
        return self.area + other.area
    
    def __str__(self):
        return(f"This Rectangle has a length of {self.length} and a width of {self.width} ")
    
    def __gt__(self, b):
        if self.area > b.area:
            return True
        else:
            return False
        


rect1 = Rectangle(2,4)




print(rect1.width)

