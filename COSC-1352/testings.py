from tkinter import *
from tkinter import PhotoImage


class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()
        
     # sets up the GUI
    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", \
                             height=8, width=15)
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
        img = PhotoImage(file="COSC-1351/COSC-1352/images-gif/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, \
                        highlightthickness=0, activebackground="white", command=lambda:self.process("("))
        button.image = img
        button.grid(row=1, column=0, sticky=N + S + E + W)
        
        

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
