#####################

#Name: Chiedozie Ehileme

#Date: September 26, 2022

#Description: Drawing multiple shapes

#####################

import turtle

# screen properties
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("My Beautiful drawing")  # type: ignore

# define turtle(s)
t = turtle.Turtle()
s = turtle.Turtle()

# t.pen properties
s.pen(pencolor="blue",speed=10,pensize=3)



#### DRAWING A EQUALATERAL TRIANGLE
s.penup()
s.setposition(100,100)
s.pendown()

for i in range(3):

    s.forward(100)
    s.left(120)


### DRAWING A SQUARE

s.penup()
s.setposition(-250,195)
s.pendown()

for i in range(4):
    
    s.forward(100)
    s.right(90)

### DRAWING A HEXAGON

s.penup()
s.setposition(-250,-120)
s.pendown()

for i in range(6):

    s.forward(80)
    s.right(60)

### DRAWING A OCTAGON

s.penup()
s.setposition(180,-130)
s.pendown()

for i in range(8):
    s.forward(59)
    s.right(45)


## used to keep GUI window open in Visual Studio Code
screen.exitonclick()