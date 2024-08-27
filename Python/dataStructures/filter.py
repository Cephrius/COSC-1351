def f(x):
    return (x %3 == 0 or x %5 == 0)

multiples = filter(f, range(3,46))

for i in multiples:
    print(i)