
class Fraction(object):
    # by Default, a fraction is 0/1
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den


    # getter for the numerator
    @property
    def num (self):
        return self._num

    # setter for the numerator
    @num.setter
    def num(self, value):
        self._num = value

    # getter for the den
    @property
    def den(self):
        return self._den
    # setter for the denominator
    @den.setter
    def den(self, value):
        # ignore if the specified denominator is 0
        if (value != 0):
            self._den = value

    # return a fraction's numeric
    # representation
    def getReal(self):
        return float(self.num / self.den)

    # main Program
f1 = Fraction()
f2 = Fraction(3,2)
f3 = Fraction(0,3)

print(f"{f1.num}/{f1.den} = {f1.getReal()}")
print(f"{f2.num}/{f2.den} = {f2.getReal()}")
print(f"{f3.num}/{f3.den} = {f3.getReal()}")