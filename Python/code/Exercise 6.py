#####################

#Name: Chiedozie Ehileme        

#Date:  September 26, 2022

#Description: Changing pen color based on user input

#####################

import turtle

# screen properties
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("My Beautiful drawing")  # type: ignore

# define turtle(s)
s = turtle.Turtle()

pencolors = input("Pick a colour to draw a square: \n Blue\n Red\n Orange: ")


# Defining a square function
def square():
    s.penup()
    s.setposition(-100,100)
    s.pendown()
   
    for i in range(4):
        s.forward(100)
        s.right(90)

s.pen(pensize=3)

# Chosing Colours and drawing shapes:

if(pencolors == "Orange"):
            s.pen(pencolor="Orange")
            square()
elif(pencolors == "Red"):
                s.pen(pencolor="Red")
                square()
elif(pencolors == "Blue"):
                s.pen(pencolor = "Blue")
                square()
else:
        print("That not a colour choice....")
        


## used to keep GUI window open in Visual Studio Code
screen.exitonclick()      