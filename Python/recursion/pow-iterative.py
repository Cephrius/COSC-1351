# x^y

x = int(input("Enter the Base: "))
y = int(input("Enter the exponent: "))
pow = 1

for i in range(0, y):
	pow *= x

print ("{}^{} = {}".format(x, y, pow))

