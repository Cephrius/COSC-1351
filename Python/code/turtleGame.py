 ########################################

#Name: Chiedozie Ehileme

#Date: October 3, 2022

#Program Description: Created a game using the turtle library

#Extra Credit: None or explain what you did for the extra credit

########################################


import turtle
import random

# Setting the background to black
turtle.bgcolor("Black")


# Showing our turtle screen 
screen = turtle.getscreen()



# Declaring our varibles

leftBound = -screen.window_width() / 2 
rightBound = screen.window_width() / 2 
topBound = screen.window_height() / 2 
bottomBound = -screen.window_height() / 2 

# declare a name and color for your turtle

player1 = input("Enter a name for player 1: ")
color1 = input("Enter a color for player 1: ")
player2 = input("Enter a name for player 2: ")
color2 = input("Enter a color for player 2: ")

# Creating the first player GREEN TURTLE 

t1 = turtle.Turtle()
t1.color(color1)
t1.left(90)
t1.shape("turtle")
t1.penup()
t1.goto(-200,-200)

# Creating the second player BLUE TURTLE

t2 = turtle.Turtle()
t2 = t1.clone()
t1.color(color2)
t2.penup()
t2.goto(200,-200)

# this turtle draws the finish line for the other turtles

t3 = turtle.Turtle()
t3 = t1.clone()
t3.color("Red")
t3.penup()
t3.goto(leftBound,topBound-100)
t3.pendown()
t3.goto(rightBound,topBound-100)

# Creating our dice that controls how much the turtle moves

dice = random.randint(1,6)

# Creating the game

t1.penup()
t2.penup()

for i in range(100):
    if t1.ycor()>=(topBound-100):
        print("{} Wins!".format(player1))
        break
    elif t2.ycor()>=(topBound-100):
        print("{} Wins!".format(player2))
        break
    else:
        player_one_turn = input("Press 'Enter' to move your turtle ")
        x = random.randint(leftBound, rightBound)
        y = random.randint(bottomBound,topBound)
        print(x,y)
        t1.goto(-200,y + (20 * dice)) 
        

        player_two_turn = input("Press 'Enter' to move your turtle ")
        x = random.randint(leftBound, rightBound)
        y = random.randint(bottomBound,topBound)
        print(x,y)
        t2.goto(200, y + (20 * dice))
        









# Keeps screen open in VSCode
screen.exitonclick()
