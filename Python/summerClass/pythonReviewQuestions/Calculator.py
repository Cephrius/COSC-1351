firstnumber = float(input("Enter in the first number: "))
secondnumber = float(input("Enter in the second number: "))
operator = input("Enter in a operator: ")


if operator == "+":
    sum = (firstnumber + secondnumber)
    print(f"The sum of {firstnumber} and {secondnumber} is {sum}")
elif operator == "-":
    difference = (firstnumber - secondnumber)
    print(f"The difference of {firstnumber} and {secondnumber} is {difference}")
else: 
    print("Invalid operator. Please enter a valid operator (+, -).")