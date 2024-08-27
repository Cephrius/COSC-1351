#n = 5
n=int(input("Enter a number: "))
# for i in range(1, n):
for i in range(n-1, 0, -1):
	n *= i

print (("5! = {}".format(n)))
