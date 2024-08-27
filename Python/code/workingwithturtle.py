import turtle

# screen properties
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("My Beautiful drawing")  # type: ignore

# define turtle(s)
t = turtle.Turtle()
s = turtle.Turtle()

"""
# t.pen properties
t.pen(pencolor="blue",speed=10,pensize=3)
t.penup()

t.pendown()
"""
"""
pencolors = input("Pick a colour to draw a square: \n Blue\n Red\n Orange: ")


# Defining a square function
def square():
    s.penup()
    s.setposition(-100,100)
    s.pendown()
   
    for i in range(4):
        s.forward(100)
        s.right(90)


# Chosing Colours and drawing shapes:

if(pencolors == "Blue"):
        s.pen(pencolor = "Blue")
        square()
elif(pencolors == "Orange"):
            s.pen(pencolor="Orange")
            square()
elif(pencolors == "Red"):
        s.pen(pencolor="Red")
        square()
"""            
t.pen(pencolor="Green",speed = 10, pensize=10)


"""
# loop to draw pentagon
for i in range(6):

    t.forward(-90)
    t.left(-300)
c = t.clone()
c.color("red")
c.circle(20)
"""
# cloning muultiple squares
"""
for i in range (4):
    
    t.forward(200)
    t.right(90)

# Declare 's' varible properties

s = t.clone()
s.color("orange")
s.right(5)

for i in range(4):
    s.forward(120)
    s.right(90)

# Declare 'e' varible properties

e = s.clone()
e.color("green")
e.right(5)

for i in range(4):
    e.forward(50)
    e.right(90)
print(i)
"""


"""
t.color("white")
for i in range (360):
    
    #draw squares 
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

    t.left(i)
"""


"""
#while loop

n = 10
while n <= 10 
    t.circle(n)
    n = n + 10
"""


"""
# while loop with input

n = input("Would you like to draw a circle??: ")

if n == "yes" or n == "YES" or n == "Yes" or n == "yEs" or n == "yeS" or n == "YEs" or n == "yES" or n == "YeS":
    t.circle(100)
else:
    t.dot(100)
"""



##### DRAWING A EQUALATERAL TRIANGLE
"""
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
"""





## used to keep GUI window open in Visual Studio Code
screen.exitonclick()