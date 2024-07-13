## OOP Programming

'''
######## CAR CLASS ###########
class Car:

    # define class variables here
    wheels = 4

    def __init__(self,make,model,year,colour):
        self.make = make # instance variables
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print(f"The {self.model} is driving....")

    def park(self):
        print(f"The {self.model} is parked.....")

    def __str__(self):
        return (f"The vehicle is a {self.year} {self.make} {self.model} in {self.colour}")

car1 = Car("Tesla","Model Y Performance", "2022", "Midnight Black")

print(car1.wheels)
################################################################################################
'''

####### Animal class######
'''
class Animal:

    alive = True

    def eat(self):
        print(f"This animal is eating....")

    def sleep(self):
        print(f"This animal is sleeping...")


class Rabbit(Animal):
    def run(self):
        print(f"The rabbit is running...")

class Dog(Animal):
    def bark(self):
        print(f"The dog is barking.....")

\class Bird(Animal):
    def fly(self):
        print(f"The bird is flying.....")


r1 = Rabbit()
d1 = Dog()
b1 = Bird()

r1.run()
d1.bark()
b1.fly()
'''

########## Multi inheritance ##############
"""
class Prey:

    def flee(self):
        print("The animal flees....")

class Predator:

    def hunt(self):
        print("The animal hunts....")

class rabbit(Prey):
    def flee(self):
        print("The rabbit is fleeing....")

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


r1 = rabbit()
h1 = Hawk()
f1 = Fish()

r1.flee()
"""
##########################################################

############ METHOD CHAINING ###################
"""
class car:
    def turn_on(self):
        print("You turn on the car....")
        return  self

    def drive(self):
        print("You drive the car.....")
        return self

    def brake(self):
        print("The car is braking....")
        return self

    def turn_off(self):
        print("You turn off the car.....")
        return self

car = car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
"""
##########################################################

############## SUPER FUNCTION ##########################
"""
class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

cube = Cube(3,2,1)
square = Square(2,5)

print(cube.volume())
print(square.area())
"""
##########################################################################

############# ABSTRACT CLASSES ###############################
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("The car is moving......")
    def stop(self):
        print("The car is stopped...")
class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is moving....")
    def stop(self):
        print("The motorcycle is stopped.....")



motor = Motorcycle()
Car = Car()


motor.go()
motor.stop()
Car.go()
Car.stop()
"""
#################################################


################# OBJECTS AS ARGUMENTS ####################
"""
class Car:

    colour = None

class Motorcycle:

    colour = None
def change_colour(vehicle,colour):
    vehicle.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_colour(bike_1,"Blue")
change_colour(bike_2,"Yellow")
change_colour(bike_3,"Orange")

change_colour(car_1,"Blue")
change_colour(car_2,"Yellow")
change_colour(car_3,"Orange")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)

print(bike_1.colour)
print(bike_2.colour)
print(bike_3.colour)
"""
#####################################################################

############## DUCK TYPING ##########################
"""
class Duck:
    def walk(self):
        print("This duck is walking.")

    def talk(self):
        print("This duck is qwuacking.")

class Chicken:
    def walk(self):
        print("This Chicken is walking.")

    def talk(self):
        print("This chicking is Clucking.")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
"""
#####################################################################

############# WALRUS OPERATROR ###############

"""
foods = list()

while True :
    food = input("What foods do you like?: ")
    if food == "quit":
        break
    foods.append(food)
"""

"""foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
print(foods)"""


#####################################################################

########### ASSIGNING VARIBLES TO FUNTIONS #####################
'''
def hello():
    print("Hello")

hi = hello
hi()

say = print
say("This is crazy its like creating your own programming language")
'''
#############################
####### HIGHER ORDER FUNCTION ######################
"""
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
     text = func("Hello")
     print(text)

hello(loud)
hello(quiet)
"""

########### PART 2 ###################

"""def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(4)
print(divide(10))"""


"""def divide(x):
    return x / divisor
divisor = 3

print(divide(15))"""

############## LAMBDA FUNCTION ###################
# Funtion that is writing in one line
#lambda paramerters : expression

#def double(x):
    #return x * 2

#print(double(5))

"""
double = lambda x: x * 2
print(double(3)) 
"""

"""
multiply = lambda x, y : x * y
print(multiply(5,5))

add = lambda x,y,z: x + y + z
print(add(3,5,1))

full_name = lambda first_name, last_name : first_name+" "+last_name
print(full_name("Chiedozie","Ehileme"))

age_check = lambda age: True if age >= 18 else False
print(age_check(12)) 

"""

#######################################################


########### SORT IRITIBLES ##########################
"""
students = ("Squidward", "Sandy", "Patrick", "Spongebob","Mr.Krabs")

#students.sort(reverse = True) 
sorted_students = sorted(students, reverse=True)
print(sorted_students)
"""

############ LEVEL 2 ###########################
"""
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs","C", 78))

name = lambda names: names[0]
grade = lambda grades: grades[1]
age = lambda ages: ages[2]

sorted_students = sorted(students, key = name , reverse = False)

for student in sorted_students:
    print(student)

    
students.sort(key = age)
for student in students:
    print(student)
"""

#######################################

################## MAP FUNCTION ##################
# applies a function to each item in a iterable (list, tuple,etc)

"""
store = [("shirt", 20.00),
        ("pants", 25.00),
        ("jacket", 50.00),
        ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_usd = lambda data: ((data[0],data[1]/0.82))

store_euros = list(map(to_euros,store))                
store_usd = list(map(to_usd,store))

for item in store_euros:
    print(item)

for item in store_usd:
    print(item)

"""
###########################################
############ FILTER FUNCTION #########################

# creates a collection of elements from an iterable for which a function returns true
# filter(funcion, iretable)
"""
friends = [("Rachel",19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler",21),
           ("Ross", 20)]


over_18 = lambda ages: ages[1] >= 18
able_to_drink = filter(over_18, friends)

for i in able_to_drink:
    print(i)
"""

###########################################
############### REDUCE ######################

# applies a function to an iterable and reduce it to a single cumulative value.
# performs functiuon on first two elements are repeats process until 1 value remains

# reduce(function, iterable)
"""
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y:x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x * y,factorial)
print(result)

"""
###########################################
########### LIST COMPREHENSTION ##############

# a way to create a new list with less syntax that can mimic certain lambda funciton, 
# easier to read 
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable if conditional]
"""

squares = []   # create an empty list
for i in range(1,11):      # create a for looop
    squares.append(i * i)   # define what each loop iteration should do 
print(squares)              # print results


list = [i * i for i in range(0,11,2)]
print(list)



students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x : x >= 60,students))

pass_student = [i for i in students if i >= 60]

pass_students = [i if i >= 60 else "Failed" for i in students]
print(pass_students)
"""
###########################################
########## Dictonary Comprehension ##############
"""
# Create dictionaries using an expression which can replace
# for loops and certain lambda functions

# dictionary = {key : expression for (key, value) in iterable}
# dictionary = {key : expression for (key, value) in iterable if conditional}
# dictionary = {key : (if/else) for (key, value) in iterable}
# dictionary = {key : function(value) for (key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cites_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}
weather = {'New York': "Snowing", 'Boston': "Sunny", 'Los Angeles' :  "Sunny", 'Chicago': "Cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "Sunny"}

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

is_warm = {key: ("Warm" if value > 85 <= 89 else "Too Cold")  for(key, value) in cities.items()}

def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"

desc_cities = {key: check_temp(value)  for(key, value) in cities.items()}

print(desc_cities)
print(cites_in_C)
print(sunny_weather)
print(is_warm)
"""
###########################################
############# ZIP FUNCTION ##################################
"""
# aggregate elements from two or more iretables (list,tuple,sets, dicts,etc.)
# creates a zip object with paried elements stored in tuples for each element
# zip(*iterables)

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","2/5/2019","4/7/2008"]

users = zip(usernames,passwords,login_date)

for i in users:
    print(i)

print(type(users))
for key,values in users.items():
    print(f"{key} : {values}")

"""
###########################################
######## if __name__ == "__main__': ##################

# y tho
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by oterh modules

# python interpreter sets "special variables", one of which is __name__
# then python will execute the ocde found within __main__

def hello():
    print("Hello!")

if __name__ == '__main__':
    pass

##############################################################
####### TIME MODULE/ LIBRARY #################################

"""
import time

print(time.ctime(1000000000)) # Convert a time expressed in seconds since epoch to a readable string
#                      epoch = when your computer thinks time began (reference point)
print(time.time())
print(time.ctime(time.time()))

time_object = time.localtime()
time_object = time.gmtime() # UTC Time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = "20 April, 2020"
time_object =time.strftime(time_string,"%d %B, %Y")


# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020,4,20,4,20, 0,0,0,0)
time_string = time.asctime(time_tuple)

print(time_string)

"""




################################################################################
############ MULTI THREADING ###################
"""
# thread = a flow of exectution. Like a seperate order of instructions. 
#          However each thread take a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold control of the python interpreter
#
# cpu bound = program/tasks that spends most of its time wating for internal events (cpu intensive)
#             use multiprocessing
#
# io bound = program/tasks that spends most of its time wating for external events (user inputs)
#            use multithreading


import threading
import time 

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(5)
    print("You drink coffee")
def take_shower():
    time.sleep(7)
    print("You take a shower")

x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee())
y.start()

z = threading.Thread(target=take_shower())
z.start()

x.join()
y.join()
z.join()

eat_breakfast()
drink_coffee()
take_shower()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

"""
#####################################################################
######## DAEMON THREADING #############################

# deamon thread = a thread that runs in the background, not important for program to run 
#                 your program will not wait for daemon threads to ocmplete before exiting
#                 non-daemon threads cannot normally be killed,stay alive untill task is complete

#
#                ex. background tasks, garbage collection, waiting for imput, long running processes
"""
def timer():
    print()
    count = 0
    while True:
        import time
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")

import threading
x = threading.Thread(target=timer, daemon= True)
print(x.isDaemon())
x.setDaemon(True)
x.start()

answer = input("Do you wish to exit?? \n")

"""
##########################################################
################ MULTIPROCESSING ####################

#multiprocessing = running tasks in parallel on different CPU cores, bypass GIL used for threading
#                  better for cpu bound tasks (heavy CPU usage)
#                  multithreading = better for io bound tasks (waiting around)
"""
from multiprocessing import Process, cpu_count
import time

def counter(num):
     count = 0
     while count < num:
         count += 1
def main():

    print(cpu_count())

    a = Process(target=counter,args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter,args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter,args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter,args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    counting = round(time.perf_counter()/1000)
    print(f"Finished in: {counting} seconds")

if __name__ == '__main__':
    main()
time.perf_counter()

"""
###############################################################
############## GUI WINDOWS ####################
from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
"""
window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Our GUI")
window.config(background= "lightBluell")

icon = PhotoImage(file='Capture001.png')
window.iconphoto(True,icon)

window.mainloop() # place window on computer screen
"""

########### LABELS ################
# label = an area widget that holds text and or other within a window\
"""
window = Tk()

photo = PhotoImage(file='download.png')

label = Label(master= window,
              text= "Hello World",
              font=('Arial',40,'bold'),
              fg='lightBlue',bg='Black',
              relief=RAISED,
              bd=10,
              padx= 20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x = 200, y = 0)


window.mainloop()

"""
#####################################################
######## BUTTON ###############
# button = you click it, it does stuff
"""
def click():
    global count
    count += 1
    print(f'{count}')

window = Tk()

count = 0

photo = PhotoImage(file='download.png')

button = Button(window,
                text= "Click Me !!",
                command=click,
                font=("Comic Sans", 30,),
                fg='lightBlue',
                bg='Black',
                activeforeground='lightBlue',
                activebackground='Black',
                state = ACTIVE,
                image=photo,
                compound='bottom')

button.pack()

window.mainloop()

"""
######################################################
############ ENTRY BOX ############
"""
window = Tk()

entry = Entry(window,
              font=('Comic Sans',50),
              fg= 'lightBlue',
              bg='Black'
              ,show="*")# <---- allows you to replace the text entered with specifed character... like a password that is hidden
#entry.insert(0,) # <------ you can add text here that is appears when ran
entry.pack(side=LEFT)

def showPassword():
    entry.config(show=ACTIVE)
def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)

show_Password = Button(window,
                       text= "Show",
                       command=showPassword)

submit_button = Button(window,
                       text = "Submit",
                       command=submit)
delete_button = Button(window,
                       text = "Delete",
                       command=delete)
backspace_button = Button(window,
                       text = "Backspace",
                       command=backspace)


submit_button.pack(side= RIGHT)
backspace_button.pack(side= RIGHT)
delete_button.pack(side= RIGHT)
show_Password.pack(side= RIGHT)


window.mainloop()

"""

###############################################################
################# CHECK BUTTONS ##################
"""
def display():
    if (x .get() == "YES"):
        print("You agree!! ")
    else:
        print("You dont agree! ")

# you first have to instanciate a window before you add attributes to the window
window = Tk()
icon = PhotoImage(file="download.png")
window.title("Do you Agree")
window.iconphoto(True,icon)

#x = BooleanVar() # <---- Returns True or False
# x = IntVar() # <------- Returns a 1 or 0
x = StringVar() # <------ Returns a string value

pythonPhoto = PhotoImage(file="download.png")

checkButton = Checkbutton(window,
                          text= " I agree to something",
                          variable= x,
                          onvalue="YES",
                          offvalue="NO",
                          command=display,
                          font=("Comic Sans", 20),   # <------ Like CSS but in python
                          fg = "lightBlue",
                          bg="Black",
                          activeforeground="lightBlue",
                          activebackground="Black",
                          padx= 25,
                          pady= 10,
                          image=pythonPhoto,
                          compound=LEFT,
                          )
checkButton.pack()
window.mainloop()
"""

##################################################
########## RADIO BUTTONS ####################
"""
# radio button = similar to checkbox, but you can only select one from the group
def Order():
    if x.get() == 0:
        print("You order pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get () == 2:
        print("You ordered a hotdog")
    else:
        print("huh?")


foods = ["pizza", "hamburger", "hotdog"]

window = Tk()

pizzaImage = PhotoImage(file="download.png")
hamburgerImage = PhotoImage(file="download.png")
hotdogImage = PhotoImage(file= "download.png")

foodImages = [pizzaImage,hamburgerImage,hotdogImage]
x = IntVar()

for index in range(len(foods)):
    radio_button = Radiobutton(window,
                               text= foods[index], # Adds text to radio buttons
                               variable=x, # create a variable that all the buttons share groups them together
                               value=index # gives the buttons their own values
                               ,padx=25, # adds padding on the x-axis
                               font=("Comic Sans",20), # add a font to the text
                               image= foodImages[index] # adds image to the radioButtons
                               ,compound=LEFT   # Formats the orientation of the images and text
                               ,indicatoron = 0  # eliminate circle indicators
                               , width =450 # sets the width of the radioButtons
                                ,command = Order # set command of radiobutton to function
                               )
    radio_button.pack(anchor=W)

window.mainloop()


"""
###############################################################
########### SCALE ###########
"""
def submit():
    print(f"The temperature is: {scale.get()} degrees C")

window = Tk()

hotImage = PhotoImage(file='download.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,from_= 100,
              to = 0,
              length= 600, # <---------- Length of scale
              orient= VERTICAL,# <------ Orientation of scale
              font=("Comic Sans", 20)
              ,tickinterval= 10, # <---------- displays interval on scale
              showvalue=0, # <---------- Hides current value
              troughcolor = '#69EAFF',
              fg='#FF1C00',
              bg="Black",
              )
scale.set(((scale['from']-scale['to'])/2) + scale['to']) # <----- Sets the middle of the slider regardless of any number
scale.set(0) # <----- Sets the value of any number

button = Button(window,
                text="Submit",
                command=submit,
                font=("Comic Sans",10)
                )

scale.pack()

coldImage = PhotoImage(file='download.png')
coldLabel = Label(image =coldImage)
coldLabel.pack()


button.pack()
window.mainloop()
"""
#########################################
############ LIST BOX ########################
"""
# listbox = a listing of selectable text items within it's own container

# FUNCTIONS WE CREATED
def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print(f"You have ordered: ")
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(),entry_box.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed (listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

# CALL YOUR WINDOW
window = Tk()
window.title("Our Menu")

listbox = Listbox(window,
                 bg="#f7ffde",
                 font=("Constantia",35),
                  width=12,
                  selectmode = MULTIPLE
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")



listbox.config(height= listbox.size())


entry_box = Entry(window)
entry_box.pack()

# Submit Button
submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack()

# Add Button
add_button = Button(window,
                       text="Add",
                       command=add)
add_button.pack()

# Delete Button
delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack()

window.mainloop()

"""
"""
###############################################################
######### MESSAGE BOXES #########################################

from tkinter import messagebox #import the messages box library

def click():
    #messagebox.showinfo(title= " This is a info message box",
                       #message= "You are a person")

    #messagebox.showwarning(title= "WARNING !!"
                           #,message= "You have a VIRUS !!! ")

    #messagebox.showerror(title = "This is an error",
                         #message= "This is a warning")

    #if messagebox.askokcancel(title = "ask ok cancel"
                          # ,message="Do you want to do the thing?"):
        #print('You did a thing')
    #else:
       # print("You canceled a thin                             #message= 'Do you want to retry the thing?'):
        #print('You retried the thing.')
    #else:
        #print('You cancelled a thing!')

    #if messagebox.askyesno(title = "Ask yes or no",
                       # message = "Do you like cake."):
        #print("I like cake too! ")
    #else:
      #  print("Why do you hate Cake?")

    #answer =  messagebox.askquestion(title = 'Hello There',message = 'Do you like pie?? ')

    #if answer == 'yes':
        #print("I like pie too....")
    #else:
        #print("Why dont you like pie?? ")
    
    #answer = messagebox.askyesnocancel(title="Asking a quesetion", message="Do you like to code",icon= 'warning') # <---- icon can only be error,info, quesiton, or warning 
    #if answer == True:
      #  print("You like to code")
   # elif answer == False:
     #   print("Then why are you learning to code")
   # else:
    #    print("You have dodged the question..")

window = Tk()

button = Button(window,
                command=click,
                text = "Click me ")
button.pack()


window.mainloop()

"""

#################### Colour Chooser #########################
"""
from tkinter import *
from tkinter import colorchooser # submodule

def click():
    window.config(bg=colorchooser.askcolor()[1]) # Change background colour
    

window = Tk()
window.geometry("420x420")


button = Button(text= "Click Me", command = click)
button.pack()




window.mainloop()

"""



##########################################################
###################### TEXT WIDGET #######################
# functions like a text area, you can enter multiple line of text \
"""
from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)


window = Tk()

text = Text(window,
            background= "lightyellow",
            font=("Comic Sans",15),
            padx=20,
            pady=20)

button = Button(window,
                command = submit,
                text = "Submit")



text.pack()
button.pack()
window.mainloop()

"""
#######################################################################
#################### Open a file ###############################
"""

from tkinter import*
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:/Users/theac/OneDrive/Documents/COSC-1351/Python/code",
                                          title="Open File",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,"r")
    print(file.read())
    file.close()
    
    
window = Tk()

button = Button(window,text = "Open", command = openFile)

button.pack()
window.mainloop()

"""
###########################################################################
############################# SAVING A FILE ############################
"""
from tkinter import*
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\Python\\code",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text File",'.txt'),
                                        ("HTML File",'.html'),
                                        ("CSS File",'.css'),
                                        ("All Files",'.*'),
                                    ])
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text: ")  #<----- I can write out text to the file from the console window..... 
    file.write(filetext)
    file.close()

    # prevent errrors 
    if file is NONE:
        return


window = Tk()


button = Button(window,text = "Save", command = saveFile)
text  = Text(window)


button.pack()
text.pack()
window.mainloop()"""

#####################################################################
######################### MENUBAR #################################
"""
from tkinter import*

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def exitFile():
    print("File has been closed!")
    
def cut():
    print("You cut some text!")

def copy():
    print("You copied some text")

def paste():
    print("You copied some text!")

window = Tk()
window.title("Menubars")

# Images
exitImage = PhotoImage(file = "Python/code/broCode/exit.png")
saveImage = PhotoImage(file = "Python/code/broCode/save.png")
openImage = PhotoImage(file = "Python/code/broCode/openfile.png")



menubar = Menu(window)
window.config(menu = menubar)

# File menu
fileMenu = Menu(menubar,tearoff = 0) #font = ("Aerial", 15) # <---- You can add fonts
menubar.add_cascade(label = "File", menu = fileMenu)     #<----- Add new meundrop list to menubar
fileMenu.add_cascade(label = "Open",command = openFile, image = openImage, compound ='left')
fileMenu.add_cascade(label = "Save",command = saveFile, image = saveImage, compound ='left')
fileMenu.add_separator()
fileMenu.add_cascade(label = "Exit", command = exitFile, image = exitImage, compound ='left')

#edit menu
editMenu = Menu(menubar,tearoff = 0 )#font = ("Aerial", 15) # <---- You can add fonts
menubar.add_cascade(label = "Edit", menu = editMenu) # <----- Add new meundrop list to menubar
editMenu.add_command(label = "Cut" ,command = cut)
editMenu.add_command(label  = "Copy", command = copy)
editMenu.add_command(label = "Paste", command = paste)


window.mainloop()
"""
#####################################################################################################

##################### FRAMES ####################################################################
"""
# frame = a rectangualr container to gorup and hold widgets


from tkinter import *

master = Tk()

frame = Frame(master,bg = "pink", bd = 5,relief = SUNKEN)
frame.place(x = 100, y = 100) #<------- Used this to stick frame at certain location
#frame.pack(side = BOTTOM)


Button(frame,text="W",font=("Consolas", 25),width=3).pack(side = TOP)
Button(frame,text="A",font=("Consolas", 25),width=3).pack(side = LEFT)
Button(frame,text="S",font=("Consolas", 25),width=3).pack(side= LEFT)
Button(frame,text="D",font=("Consolas", 25),width=3).pack(side = LEFT)


master.mainloop()
"""

#########################################################################################################


####################### NEW WINDOWS #####################################################################
"""
from tkinter import *

def create_window():
    new_window = Tk() #<--------- New window ontop of other windows. linked to bottom window
    # new_window = TopLevel() #<--------- New window not linked to other windows, new instances of Tk()
    old_window.destroy()    # <------- Closes old window


old_window = Tk()

Button(old_window,text="create new window",command = create_window).pack()

old_window.mainloop()


"""
#######################################################################################################

############### WINDOW TABS ##########################################################################
"""
from tkinter import *
from tkinter import ttk
 
window = Tk()

notebook = ttk.Notebook(window) # <------ Widget that manages a collection of windows / displays 

tab1 = Frame(notebook) #<----- New frame for tab 1
tab2 = Frame(notebook) #<----- New frame for tab 2

notebook.add(tab1,text ="Tab1")
notebook.add(tab2,text ="Tab2")
notebook.pack(expand = True,fill = "both") #<------ expand to fill any space not otherwise used
                                           #<------- fill space on x and y axis 

Label(tab1,text = "Hello this is tab number 1", width=50,height = 25).pack()
Label(tab2,text ="Goodbye this is tab number 2", width=50,height = 25).pack()

window.mainloop()
"""

######################################################################################################
##################### GRID ##########################################################################
"""
from tkinter import *
# grid() = geometry manager that organizes widgets in a table-like structure in a parent window

window = Tk()
window.title("Enter Your Info")

<<<<<<< HEAD
titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column= 0,columnspan=2)
=======
titleLabel = Label(window,text="Enter your info", font=("Arial",25)).grid(row=0,column=0, columnspan=2)
>>>>>>> bfb77cde603618762489d9e61e467d1b924fc81a

firstNameLabel = Label(window,text= "First Name: ",width=20,bg="red").grid(row = 1, column = 0)
firstNameEntry = Entry(window).grid(row=1,column =1)

LastNameLabel = Label(window,text= "Last Name: ",bg="green").grid(row = 2, column = 0)
LasttNameEntry = Entry(window).grid(row=2,column =1)

<<<<<<< HEAD
emailLabel = Label(window,text= "Email: ",bg="lightBlue",width=30).grid(row = 3, column = 0)
emailEntry = Entry(window).grid(row=3,column =1)

sumbitButton = Button(window, text= "Submit").grid(row = 4,column = 0,columnspan=2)

window.mainloop()
"""
##############################################################################################
################ Progress Bar ###############################################################
"""
from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while(download < GB):
        time.sleep(0.05)
        bar["value"]+=(speed/GB)*100
        download += speed
        percent.set(str(int((download/GB) * 100)) + "%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text = "Download",command=start).pack()






window.mainloop()


"""
##############################################################################################
################### Canvas ###################################################################

# canvas = widget that is used to draw images plots, etc

from tkinter import *

window = Tk()

canvas = Canvas(window,height=550,width=550)

canvas.create_arc(0,0,500,500,fill = "red",extent =180,width =10)
canvas.create_arc(0,0,500,500,fill = "white",extent = 180,width = 10,start =180)
canvas.create_oval(190,190,310,310,fill = "white",width=10)
canvas.create_oval(210,210,290,290,fill = "#FFFFF8",width=5)
canvas.pack()
=======
emailLabel = Label(window, text="email: ",bg="blue",width=30).grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
>>>>>>> bfb77cde603618762489d9e61e467d1b924fc81a


window.mainloop()