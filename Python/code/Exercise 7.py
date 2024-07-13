#####################

#Name: Chiedozie Ehileme

#Date: September 26, 2022

#Description: Recreated minecraft steve's face

#####################

import turtle

# screen properties
screen = turtle.getscreen()
screen.bgcolor("white")
screen.title("Steve")  # type: ignore

# define turtle(s)
t = turtle.Turtle()
t.hideturtle()

t.pen(speed=50)

#define square
def square():
    t.penup()
    t.setpos(-300,200)
    t.pendown()
    for i in range(4):
        t.forward(600)
        t.right(90)
    
#define steve's hair
def stevehairline():
    t.penup()
    t.setpos(-300,200)
    t.pendown()  
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(100)
        t.right(90)

def sidburns():
    t.penup()
    t.setpos(-300,100)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
    
    t.penup()
    t.setpos(200,100)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)

# Define steves' eye
def eyes(): 
    t.pen(fillcolor="white")
    t.penup()
    t.setpos(-200,-85)
    t.pendown()
    
    t.begin_fill()
    for i in range(2):
        t.forward(130)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    
    t.penup()
    t.setpos(90,-85)
    t.pendown()
    
    t.begin_fill()
    for i in range(2):
        t.forward(130)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

# Define steves' irises
def iris():
    t.pen(fillcolor="darkslateblue")
    t.penup()
    t.setpos(-130,-85)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(60)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

    t.penup()
    t.setpos(90,-85)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(60)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

# defines nose and upper lip    
def nose():
    t.pen(fillcolor="sienna")
    t.penup()
    t.setpos(-50,-165)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(120)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    
    t.pen(fillcolor="peru")
    t.penup()
    t.setpos(-50,-180)
    t.pendown()
    
    t.begin_fill()
    for i in range(2):
        t.forward(120)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

# defines steves' mouth
def mouth():
    t.penup()
    t.setpos(-115,-300)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    
    t.penup()
    t.setpos(-115,-250)
    t.pendown()

    t.begin_fill() 
    for i in range(2):
        t.forward(65)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

    t.penup()
    t.setpos(70,-250)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.forward(65)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

   
    
       
   

#Creating steves face background
t.begin_fill()
t.pen(fillcolor="sandyBrown")
square()
t.end_fill()

#creating steves hair
t.begin_fill()
t.pen(fillcolor="saddlebrown")
stevehairline()
t.end_fill()

t.begin_fill()
t.pen(fillcolor="saddlebrown")
sidburns()
t.end_fill()

# Call for eyes
eyes()

# Call for irises
iris()

# Call for nose
nose()

# Call for mouth
mouth()



## used to keep GUI window open in Visual Studio Code
screen.exitonclick() 
