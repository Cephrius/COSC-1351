

# MAP FUNCTION

def f(x):
    return x * x

squares = map(f, range(1,10))

for int in squares:
    print(int, end=", ")


str_nums = ["2","3","6","9"]
print(str_nums)
def f(x):
    return int(x)
int_nums = map(int, str_nums)
print(list(int_nums))