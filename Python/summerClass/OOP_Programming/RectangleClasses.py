class Rectangle:
    
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        self.area = length * width
        
    
    def set_area(self, length, width):
        return self.length * self.width
    
    def set_length(self, length): 
        if length > 0:
            self.length = length
            self.area = length * self.width
        else:
            raise ValueError("Length must be greater than 0")
        
    def get_length(self):
        return self.length
    
    def add_area(self, area):
        return self.area + area
    
    def __add__(self,other):
        return self.area + other.area
    
    def __str__(self):
        return(f"This Rectangle has a length of {self.length} and a width of {self.width} ")

r1 = Rectangle(4,4)
r2 = Rectangle(5,3)

total_area1 = r1.area + r2.area


print(total_area1)
print(r1)

