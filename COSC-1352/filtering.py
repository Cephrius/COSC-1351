# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
    
    
# sequence
sequence = ['g', 'e','e','j','k','s','p','r']

# using filter function
filtered = filter(fun, sequence)

print("The filtered letters are: ")
for s in filtered:
    print(s)
    
    
A = [3,4,1,4,1,4,5,4,7,4,7,3,4,3]
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
even = filter(isEven, A)
for i in even:
    print(i, end=", ")
    
    
def f(variable):
    if variable % 3 ==0 or variable % 5 == 0:
        return True
    else:
        return False


# using filter function
multiples = filter(f, range(3,31))

for m in multiples:
    print(m, end=", ")
    
    
