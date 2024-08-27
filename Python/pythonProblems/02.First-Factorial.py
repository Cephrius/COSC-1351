# Have the function FirstFactorial(num) take the num parameter being passed and
# return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the
# test cases, the range will be between 1 and 18.


# COMPLETE

def FirstFactorial(num):
    fac = 1
    for i in range (1, num + 1):
        fac = fac * i 
    return fac
 
print(FirstFactorial(5))   

