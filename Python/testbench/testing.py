"""import random


## Python number Guessing Game

guessed_number = random.randint(1,50)

while True:
    player1_points = 0
    player2_points = 0

    print(guessed_number)
    player1 = int(input('Player 1, Guess the number between 1 and 50: \n'))
    if player1 == guessed_number:
        print("Player1 guessed the Correct number, Plus 1 point \n")
        player1_points += 1
        guessed_number = random.randint(1, 50)
    elif player1 != guessed_number:
        print("Incorrect number \n")
        player2 = int(input('Player 2, Guess the number between 1 and 50: \n'))
        if player2 == guessed_number:
            print("Player2 guessed the Correct number, Plus 1 point \n")
            player2_points += 1
            guessed_number = random.randint(1, 50)
        elif player2 != guessed_number:
            print("Incorrect number \n")


    if player1_points == 1:
        print("Player 1 Wins")
        break
    elif player1_points == 1:
        print("Player 2 Wins")
        break

"""

import random

"""
start_number = 10000000

for i in range(1 , start_number):
    coin = random.randint(0,1)
    if coin == 1:
        start_number += 1

print(start_number)
"""


number = random.randint(1,259)

print(number)