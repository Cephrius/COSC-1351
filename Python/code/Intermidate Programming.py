#### Shape Class #########

class Shape(object):
    def __init__(self,bColour, fColour):
        self.borderColour = bColour
        self.fillColour = fColour

    @property
    def borderColour(self):
        return self._borderColour

    @borderColour.setter
    def borderColour(self,value):
        self._borderColour = value

class Triangle(Shape):
    def __init__(self,bColour,fColour,base,height):
        Shape.__init__(self,bColour,fColour)
        self.triangleBase = base
        self.triangleHeight = height

    @property
    def triangleHeight(self):
        return self._triangleHeight

    @triangleHeight.setter
    def triangleHeight(self,high):
        self._triangleHeight = high

    @property
    def triangleBase(self):
        return self._triangleBase

    @triangleBase.setter
    def triangleBase(self, bas):
        self._triangleBase = bas

t1 = Triangle('Blue','black',2,4)