
def even(n):
    return n % 2 == 0

evenNum = list(filter(even ,range(0,11)))
print(evenNum)


# using the map function construct a list that contians all factorials from 0 to 10 including 10

import math

factorial = list(map(math.factorial, range(11)))
print(factorial)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

factorialList = list(map(factorial, range(11)))
print(factorialList)
