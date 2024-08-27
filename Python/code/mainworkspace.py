
'''
a = 12
b = 15
c = a << 2

print(a&b)
'''

"""
a = [2,4,5,6,1]
b = [2,5,12,6,7]

print(a |= b)
"""
'''
#################
## Excersise 3 ##
#################

def getSmaller (num1 , num2):
    if num1 < num2:
        smaller = num1 
    else:
        smaller = num2
    return smaller

def main():
    userInput1 = int(input("Enter a number: "))
    userInput2 = int(input("Enter a second number: "))

    smallerNumber = getSmaller(userInput1,userInput2)
    print("The smaller of the two numbers is", smallerNumber)   

main()
'''
'''
#################
## Excersise 4 ##
#################

import math

def getQuardratic(a,b):
    square = a**2 + b**2 m
    squareRoot = math.sqrt(square)

    return squareRoot

def main():
    print("The square root of the sum of the squares of 4 and 4 is: ",getQuardratic(4,4))

############ CALL TO MAIN() ################
main()
'''

'''
################################ LISTS REVIEW ##########################################
total = 0


#1- Create a is of 5 integers
#myList = [10,2,4,5,6]
myList = ["Marian", "Zaki", "Holmes", "John" ]

#2- Print the list
print(myList)

v = " "

#3 - Add the value 1 to each element in the list using loops
#for num in range(0,len(myList)):
 #   v = v + myList[num] + " "
   #myList[num] = myList[num] + 1

#for num in myList:
#    total += num

#- For each loop
for i in myList:
    v1 = v1 + i + " "

#4- Print the new list
print(v)
print(total)



########################################################################################
'''
#################### WRITING INTO FILES #########################################

'''
import random

inFile = open("C:\\Users\\theac\\Desktop\\nums.txt",'w')
for i in range(1000):
    x = random.randint(1,25)
    inFile.write(str(x))
    inFile.write("\n")
inFile.close()
print("Done writing in the file")
'''

'''
a = 10 

def f(x):
    a = 11
    b = 21 
    x *= 2
    print("in f(): a = {}. b = {}, x= {}".format(a,b,x))

b = 20
f(b)
print("in main: a = {}, b = {}".format(a,b))

def g():
    global a 
    a *= 1.5
    print("in g(): a = {}, b = {}".format(a,b))

g()
print("in main: a = {}, b = {}".format(a,b))
'''
########################## READING INTO FILES ##################################

'''

def main():
    sportsList = open('sportslist.txt')
    sp = sportsList.read()
    print(sp)

main()



inFile = open("nums.txt")

sum = 0
for i in range(1000):
    n = inFile.readline()
    sum += int(n)

print(sum)
inFile.close()
'''


'''
########### BUILDING A BETTER TEMP CONVERTER ##############

tempChoice = input("Enter 'c' for Celsius and 'f' for Fahrenhiet: ")
if tempChoice == "f":
    print("Coverting to Fahrenheit...")

elif tempChoice == 'c':
    print("Coverting to Celsius...")

temp = int(input("Enter the Temp: "))


if tempChoice == "f":
    finalf = temp * 9/5 + 32
    print(temp,"C° is ",finalf,"° in Fahrenheit")

elif tempChoice == "c":
    finalc = 5/9 * (temp-32)
    print(temp,"F° is ",'%.2f' % finalc,"° in Celsius")
'''



'''
# Declared Variables
myList = []
total = 0
product = 1
print("Enter your numbers to add to the list: ")

# For loop that asks for specfic amounts of numbers to enter..
for i in range(1,11):
    nums = int(input("Number {}: ".format(i)))
    myList.append(nums)

# Adds all the numbers in the list together
for num in myList:
    total += num

# Multiplies all the number in the list together
for num in myList:
    product = product * num

# Prints out the algorithims findings
print("Here is your list: {}".format(myList))
print("The sum of your array is: {}".format(total))
print("The product of your list is: {}".format(product))

# finds all the even numbers in the list
evennumbers = []
for i in range(len(myList)):
    if myList[i] % 2 == 0:
        evennumbers.append(myList[i])
print(evennumbers)
'''

'''
for i in range(1,6):
    nums = int(input("Number {}: ".format(i)))
    myList.append(nums)
print(myList)
'''




'''
#####################
## APENDING A LIST ##
#####################
list = ['Mary Smith', 132, 'Jean Jones', 156, 'Karen Karter',167]

print("LIST: " ,list)
name = input("Name to add to the list: ")
average = int(input("Average: "))

list.append(name)
list.append(average)

print("UPDATED LIST: ",list)
print("There are now {} items in the list.".format(len(list)))
'''

'''

###########################
## BUILDING A CALCULATOR ##
###########################

# delcare computing methods 
def add(x,y):
    sum = x + y
    return sum

def multiply(x,y):
    product = x * y
    return product

def subtract(x,y):
    difference = x - y
    return difference

def divide(x,y):
    dividend = x / y
    return dividend

# main
num1 = int(input("What is the first number: "))
howToCompute = (input("How do you want to compute??: "))
num2 = int(input("What is the second number: "))



## assigning parameters and input for our functions()
s = add(num1, num2)
p = multiply(num1, num2)
d = divide(num1,num2)
diff = subtract(num1,num2)

## displaying output of our calculator
if howToCompute == "add":
    add(num1,num2)
    print("The sum of {} and {} is {} ".format(num1,num2,s))

elif howToCompute == "multiply":
    multiply(num1,num2)
    print("The product of {} and {} is {}" .format(num1,num2,p))

elif howToCompute == "divide":
    multiply(num1,num2)
    print("The product of {} and {} is {}" .format(num1,num2,d))
    
elif howToCompute == "subtract":
    multiply(num1,num2)
    print("The product of {} and {} is {}" .format(num1,num2,diff))

else:
    print("Please try again.....")
    
'''


'''
tempChoice = input("Enter 'c' for Celsius and 'f' for Fahrenhiet: ")
temp = int(input("Enter the Temp: "))

if tempChoice == "f":

    finalf = temp * 9/5 + 32
    print(temp,"C° is ",finalf,"° in Fahrenheit")

elif tempChoice == "c":
    finalc = 5/9 * (temp-32)
    print(temp,"F° is ",finalc,"° in Celsius")
    '''