###########################################################################################
# Name: Chiedozie Ehileme       
# Date: October 26 2024
# Description: 
###########################################################################################
from tkinter import *
from tkinter import PhotoImage
import math


# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()


    # use to calculate reciprocal 
    def calculate_reciprocal(self):
        try:
                # Get the current value from the display
                number = float(self.display["text"])
                # Calculate the reciprocal
                reciprocal = 1 / number
                # Display the result as a string
                self.display.config(text=str(reciprocal))
        except (ValueError, ZeroDivisionError):
                # Handle cases where the display is empty or when dividing by zero
                self.display.config(text="ERROR")
                
     # calcluate square root 
    def calculate_square_root(self):
        try:
                # Get the current value from the display
                number = float(self.display["text"])
                # Calculate the square root
                square_root = math.sqrt(number)
                # Display the result as a string
                self.display.config(text=str(square_root))
        except ValueError:
                # Handle cases where the display is empty or when dividing by zero
                self.display.config(text="ERROR")
                
    # now calclute percentage of a number displayed
    def calculate_percentage(self):
        try:
                # Get the current value from the display
                number = float(self.display["text"])
                # Calculate the percentage
                percentage = number / 100
                # Display the result as a string
                self.display.config(text=str(percentage))
        except ValueError:
                # Handle cases where the display is empty or when dividing by zero
                self.display.config(text="ERROR")
        
    

    # sets up the GUI
    def setupGUI(self):
    
        self.display = Label(self, text="", anchor=E, bg="white", \
                             height=8, width=15, font=('Comic Sans',24))
        self.display.grid(row=0, column=0, columnspan=5, sticky=E + W + N + S)

        #configure the rows and columns of the Frame to adjust to the window
        #there are 6 rows (0 through 5)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        #there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        # the first row
        #(
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/lpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("("))
        button.image = img
        button.grid(row=1, column=0, sticky=N + S + E + W)
        
        #)
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N + S + E + W)
        
        #AC(clear)
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("AC"))
        
        button.image = img
        button.grid(row=1, column=2, sticky=N + S + E + W)
        
        #Power (**)
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("**"))
        button.image = img
        button.grid(row=1, column=3, sticky=N + S + E + W)
        
        
        #Backspace (<---)
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/back.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white",  command=lambda: self.display.config(text=self.display["text"][:-1]))
        button.image = img
        button.grid(row=1, column=4 ,sticky=N + S + E + W)
        
        
        
        
        
	# the second row
	# 7
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N + S + E + W)
	# 8
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N + S + E + W)
	# 9
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N + S + E + W)
        
        #Square (x^2)
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/sqr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("**2"))
        button.image = img
        button.grid(row=2, column=3, sticky=N + S + E + W)
        
	# /
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.image = img
        button.grid(row=2, column=4, sticky=N + S + E + W)
        
        
	# the third row
	# 4
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N + S + E + W)
	# 5
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N + S + E + W)
	# 6
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N + S + E + W)
	# *
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("*"))
        button.image = img
        button.grid(row=3, column=4, sticky=N + S + E + W)
        
        # This function is for the sqrt of a number
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/sqrt.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.calculate_square_root())
        button.image = img
        button.grid(row=3, column=3, sticky=N + S + E + W)
                        
                        
                                
	# the fourth row
	# 1
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness = 0, activebackground = "white", command=lambda:self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N + S + E + W)
	# 2
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N + S + E + W)
	# 3
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N + S + E + W)
        
        
        # This function is for the reciprocal of a number
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/reciprocal.gif")
        button = Button(self, bg="white", image=img, borderwidth=0,
                        highlightthickness=0, activebackground="white", command=lambda: self.calculate_reciprocal())
        button.image = img
        button.grid(row=4, column=3, sticky=N + S + E + W)
        
	# -
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("-"))
        button.image = img
        button.grid(row=4, column=4, sticky=N + S + E + W)
        
        
        
	# the fifth row
	# 0
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N + S + E + W)
	# .
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N + S + E + W)
	# =
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/eql.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("="))
        button.image = img
        button.grid(row=5, column=2, sticky=N + S + E + W)
        
        # function for finding percent of a number
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/percent.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.calculate_percentage())
        button.image = img
        button.grid(row=5, column=3, sticky=N + S + E + W)
        
        
	# +
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("+"))
        button.image = img
        button.grid(row=5, column=4, sticky=N + S + E + W)

        self.pack(fill=BOTH, expand=1)
        
        

    #processes button presses
    #@staticmethod
    def process(self, button):
    # AC clears the display
        if button == "AC":
                self.display["text"] = ""
        # "=" starts an evaluation of whatever is on the display
        elif button == "=":
                expr = self.display["text"]
                try:
                        result = eval(expr)
                        self.display["text"] = str(result)
                except:
                        self.display["text"] = "ERROR!!"
        else:   
                # Concatenate the button value as a string
                self.display["text"] += str(button)


##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
