#############################################
# Name: Chiedozie Ehileme                                                                                                                                                
# Date:  FEBURARY 20, 2023                                                                                              
# Description: This assignment is intended to assess the recursive and iterative knowledge of each student.
#               Consider the recurrence relation that is defined by the following piecewise statement:                                                                                  
#############################################

print("Welcome to the recursize and iterative calculator.")
name = input("What is your first name?: ")
number = int(input(f"{name}, what number would you like to calculate using this piecewise statement?: "))

list = []

def piecewise(number):
    if number == 1:
        return 1 
    else:
      return number * (number - 1 ) + (2 * number) -1

 
print(f"The recursive value is: {piecewise(number)}")

for x in range(1,number+1):
    list.append(piecewise(x))
    
    
print(f"The iterative values are : {list}")


-