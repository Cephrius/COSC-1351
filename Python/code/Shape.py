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
        self.fillColour = fColour

    @property
    def borderColour(self):
        return self._borderColour

    @borderColour.setter
    def borderColour(self,bColour):
        self._borderColour = bColour

class Square(Shape):

    def __init__(self,bColour,fColour,length):
        Shape.__init__(self,bColour,fColour)
        self.sideLenght = length

class Circle(Shape):
    def __init__(self,c,radius = 0):
        self.radius = radius
        Shape.__init__(bColour,fColour=)