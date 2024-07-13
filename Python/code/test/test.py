from functools import reduce
def fun(x,y):
    return (x*x+y*y)

a = int(input("What is the starting number of the range: "))
b = int(input("What is the starting number of the range: "))

num = reduce(fun,range(a,b))
print(num)