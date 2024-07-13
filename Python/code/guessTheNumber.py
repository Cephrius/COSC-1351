#############################################################################
# This program asks the user for a number between 1 - 5                    #
# and uses the random library to generate a random number between 1 - 5    #
# and compares it to the users input and if correct will tell the user so, #
# and if not vice versa...                                                 #
#############################################################################

import random


def getMessage(userNum, randNum):
    if (randNum == userNum):
        print("You picked the same number as the computer!!")
    elif(randNum < userNum):
        print("Your nubmer is bigger than the computers.. try again")
    else: 
        print("Your number is smaller than the computers.. try again")
    
    return getMessage

    

def main():
    userNum = int(input("Enter a number between 1 and 5: "))
    while ( userNum > 5 or userNum < 1 ):
        userNum = int(input("Invalid number. Enter a number between 1 and 5: "))
    randNum = random.randint(1,5)
    print("Computer number: ",randNum)
    print("User number: ", userNum)
    print(getMessage(userNum,randNum))



main()