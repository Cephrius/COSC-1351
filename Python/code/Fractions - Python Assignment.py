##############################################################################
#Name: Chiedozie Ehileme                                                     #
#Date: December 5, 2022                                                      #
#Program Description: expand on the basic Fraction Object Oriented Program   #
##############################################################################
# defines a fraction
class Fraction(object):
    # by default, a fraction is 0/1
    def __init__(self, num = 0, den = 1):
        self.num = num
        # make sure not to set the denominator to 0 if specified
        if (den == 0):
            den = 1
        self.den = den

    # getter for the numerator
    @property
    def num(self):
        return self._num

    # setter for the numerator
    @num.setter
    def num(self, value):
        self._num = value

    # getter for the denominator
    @property
    def den(self):
        return self._den

    # setter for the denominator
    @den.setter
    def den(self, value):
        # ignore if the specified denominator is 0
        if (value != 0):
            self._den = value

    # returns a fraction's numeric representation
    def getReal(self):
        return float(self.num / self.den)

 
    # returns a fraction's string representation
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, self.getReal())
    
    # returns true if the self object fraction is equal to the otherFraction
    # argument object and returns false elsewise
    def __eq__(self, otherFraction):
        if Fraction == otherFraction:
                    return True
        else:
                    return False
    
    #returns true if the self object fraction is less than the other fraction
    #argument object and returns false elsewise
    def __lt__(self, otherFraction):
        if self.getReal() < otherFraction.getReal():
            return True
        else:
            return False

    # returns a fraction object that contrains the sum of the self object and the
    # otherFraction argument object

    def __add__(self, otherFraction):
        import math
        numer1 = self.num
        denom1 = self.den
        numer2 = otherFraction.num
        denom2 = otherFraction.den

        lcm  = (denom1 * denom2) // math.gcd(denom1, denom2)
        result_numer = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))
        result_denom = lcm
        return Fraction (result_numer, result_denom)
        

    # returns a fraction object that contains the result of multiplication
    #of the self object and the otherFraction argument object
    def __mul__(self, otherFraction):
       return Fraction( (self.num * otherFraction.num) , (self.den * otherFraction.den))
    
    
    #returns true if the self object is in its simplest form and false elsewise
    def simplestForm(self):
        # using the math function gcs to find the Greatest Common Denominator
        import math
        gcd = math.gcd(self.num,self.den)

        if gcd == 1:
            return True
        else:
            return False

       
### end Fraction Class definition #######    
#####################################    
######## main program ###############
# DO NOT CHANGE ANY OF THE CODE IN THE NEXT LINES #    

f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = Fraction(2,16)
print (f1)
print (f2)
print (f3)

print (f1 == f3)
print (f2 == f3)

print(f1 + f2)
print(f1 * f3)
print(f1.simplestForm())
print(f3.simplestForm())
# ADD YOUR EXTRA MAIN CODE HERE #######
num_Fractions = int(input("How many Fractions do you want to add 5 Fractions max....: "))
max_Fractions = 5
list = []
if num_Fractions > 5:
    print("Over the max amount")
for i in range(num_Fractions):
        nume = int(input(f"Enter the numerator of fraction # {str (i+1)}: "))
        deno = int(input(f"Enter the denominator of fraction # {str (i+1)}: "))
        list.append(Fraction(nume,deno))

sum = list[0]

for i in list:
    sum += i
print(f"The sum of all the fractions is: {sum}")

mul = list[0]

for i in list:
    mul *= i
print(f"The product of all the fractions is: {mul}")
