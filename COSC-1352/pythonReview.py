# # PROBLEM 1

# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
# operator = input("Enter your operator: ")

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")
    
    
# PROBLEM 2
# list = []

# #specify how many numbers the user will add to the list 
# howManyNumbers = int(input("How many numbers will you add to the list? : "))

# # add numbers to the list
# for i in range(howManyNumbers):
#     num = int(input("Enter a number : "))
#     list.append(num)

# #reverse the list 
# list.reverse()
# print(list)


# PROBLEM 3

# numbers = int(input("Enter a number: "))


# for i in range(numbers):
#     for j in range(i+1):
#         print(i+1, end="")
#     print()


# PROBLEM 4

# myList = []

# for i in range(1, 12):
#     if i % 2 == 0:
#         myList.append(i)
 
# print(myList)
    

# PROBLEM 5

countdown = int(input("Enter a number to countdown: "))

for i in range(countdown, 0, -1):
    print(i)