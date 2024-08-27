def pow(x, y):
	if (y == 0):
		return 1
	else:
		return x * pow(x, y - 1)

x = int(input("Enter the Base: "))
y = int(input("Enter the exponent: "))
print ("{}^{} = {}".format(x, y, pow(x, y)))

