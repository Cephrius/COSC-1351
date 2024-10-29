

# # MAP FUNCTION

# def f(x):
#     return x * x

# squares = map(f, range(1,10))

# for int in squares:
#     print(int, end=", ")


# str_nums = ["2","3","6","9"]
# print(str_nums)
# def f(x):
#     return int(x)
# int_nums = map(int, str_nums)
# print(list(int_nums))

from functools import reduce
A = [7,3,4,2,1]

def modify(x):
    return x + 3

def checkIFeven(x):
    return x % 2 == 0

def modify2(a,b):
    return a + b

print(list(map(modify, A)))
print(list(map(checkIFeven, A)))
print(reduce(modify2, A))


numbers = [3,5,2,4,7,1]

# min
min_value, *rest = numbers
for num in rest:
    if num < min_value:
        min_value = num
        
print( min_value)
print(rest)

# max

max_value, *rest = numbers
for num in rest:
    if num > max_value:
        max_value = num
    
print( max_value)

def findMax(a,b):
    if a > b: return a 
    else: 
        return b
    
def findMin(a, b):
    if a < b: return a
    else: 
        return b
    
    
numbers = [3,5,2,4,7,1]

print(reduce(findMax, numbers))
print(reduce(findMin, numbers))



# # REDUCE FUNCTION

a = [i for i in range(1,8)]
b = [j for j in range(1,8) if j % 2 == 0 ]

print(a)
print(b)


sum = [x + y for x in [1,2,3] for y in [3,1,4] if x != y]

print(sum)


sentence = "the quick brown fod jumps over the lazy dog"

words = sentence.split()
word_length = []

for word in words:
    if word != "the":
        word_length.append(len(word))
    
print(words)
print(word_length)
