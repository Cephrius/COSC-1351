import functools

def f(x,y):
    return x*y

fact = functools.reduce(f,range(1,10))
print(fact)