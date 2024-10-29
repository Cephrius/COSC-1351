###########################################################################################
# Name: Chiedozie Ehileme       
# Date: October 26 2024
# Description: 
###########################################################################################
from tkinter import *
from tkinter import PhotoImage


# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()

    # sets up the GUI
    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", \
                             height=8, width=15, font=('Comic Sans',24))
        self.display.grid(row=0, column=0, columnspan=4, sticky=E + W + N + S)

        #configure the rows and columns of the Frame to adjust to the window
        #there are 6 rows (0 through 5)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        #there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
        # the first row
        #(
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/0.gif")
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
	# /
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N + S + E + W)
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
	# -
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N + S + E + W)
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
	# +
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
			highlightthickness=0, activebackground="white", command=lambda:self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N + S + E + W)

        self.pack(fill=BOTH, expand=1)

    #processes button presses
    #@staticmethod
    def process(self, button):
        #AC clear the display
        if (button == "AC"):
            #clear the display
            self.display["text"] = ""
        # = starts an evaluation of whatever is on the display
        elif (button == "="):
            #get the expression in the display
            expr = self.display["text"]
            #evaluate the expresion
            try:
                result = eval(expr)
                #store the result to the display
                self.display["text"] = str(result)
            except:
                self.display["text"] = "ERROR!!"
            #note the error in the display
            #self.display["text"] = "ERROR"
        #otherwise, just tack on the appropriate operand/operator
        else:
            self.display["text"] += button


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
