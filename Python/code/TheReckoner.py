###########################################################################################
# Name: Chiedozie Ehileme
# Date: Feb 2, 2023
# Description: Making a calculator in GUI
###########################################################################################
from tkinter import *

# the main GUI
class MainGUI(Frame):
	# the constructor
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="white")
		self.setupGUI()

	# sets up the GUI
	def setupGUI(self):
		# the display 
		# right - align text in the display; and set its backgrund to white, 
		# its height to 2 charaters, and its font to 50 points
		self.display = Label(self, text= "", anchor=E, bg= "White",
		       height=5, width=15,font=("Comic Sans",30)
							)
		# put it in the top row, spanning across all four coloums; 
		# and expand it on all four sides
		self.display.grid(row=0,column=0,columnspan=4,sticky=E+W+N+S)
		#pack the GUI


		img1 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/lpr.gif")
		button = Button(self,bg='white', image=img1, borderwidth=0,
			highlightthickness=0, activebackground="white",command=lambda: self.process("("))
		
		button.image = img1
		button.grid(row=1,column=0,sticky=N+S+E+W)

		img2 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/rpr.gif")
		button = Button(self,bg= 'white', image=img2, borderwidth=0,
		  highlightthickness=0,activebackground="White",command=lambda: self.process(")"))
		
		button.image = img2
		button.grid(row=1,column=1, sticky=N+S+E+W)

		img3 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/clr.gif")
		button = Button(self,bg="white", image=img3, borderwidth=0,
		  highlightthickness=0, activebackground="White",command= lambda: self.process("AC"))

		button.image = img3
		button.grid(row = 1,column=2, sticky=N+S+E+W)

		img4 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/pow.gif")
		button = Button(self,bg = "White",image=img4,borderwidth=0,command=lambda: self.process("**"))

		button.image = img4
		button.grid(row=1, column=3, sticky=N + S + E + W)

		img5 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/div.gif")
		button = Button(self,bg = "White", image=img5,borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("/") )

		button.image = img5
		button.grid(row=2,column=3)

		img6 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/mul.gif")
		button = Button(self,bg = "White", image=img6,borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("*"))

		button.image = img6
		button.grid(row=3,column=3)

		img7 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/sub.gif")
		button = Button(self, bg="White", image=img7, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("-"))

		button.image = img7
		button.grid(row=4, column=3)

		img8 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/add.gif")
		button = Button(self, bg="White", image=img8, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("+"))

		button.image = img8
		button.grid(row=5, column=3)

		img9 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/eql.gif")
		button = Button(self, bg="White", image=img9, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("="))

		button.image = img9
		button.grid(row=5, column=2)

		img10= PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/dot.gif")
		button = Button(self, bg="White", image=img10, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda: self.process("."))

		button.image = img10
		button.grid(row=5, column=1)


		#####################
		# ADDING THE NUMBERES
		#####################

		img11 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/0.gif")
		button = Button(self, bg="White", image=img11, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("0"))

		button.image = img11
		button.grid(row=5, column=0)



		img12 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/1.gif")
		button = Button(self, bg="White", image=img12, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("1"))

		button.image = img12
		button.grid(row=4, column=0)


		self.pack(fill=BOTH, expand=1)

		img13 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/2.gif")
		button = Button(self, bg="White", image=img13, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("2"))

		button.image = img13
		button.grid(row=4, column=1)


		img14 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/3.gif")
		button = Button(self, bg="White", image=img14, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("3"))

		button.image = img14
		button.grid(row=4, column=2)

		img15 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/4.gif")
		button = Button(self, bg="White", image=img15, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("4"))

		button.image = img15
		button.grid(row=3, column=0)

		img16 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/5.gif")
		button = Button(self, bg="White", image=img16, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("5"))

		button.image = img16
		button.grid(row=3, column=1)

		img17= PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/6.gif")
		button = Button(self, bg="White", image=img17, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("6"))

		button.image = img17
		button.grid(row=3, column=2)

		img16 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/7.gif")
		button = Button(self, bg="White", image=img16, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("7"))

		button.image = img16
		button.grid(row=2, column=0)

		img16 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/8.gif")
		button = Button(self, bg="White", image=img16, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("8"))

		button.image = img16 
		button.grid(row=2, column=1)

		img16 = PhotoImage(file="C:/Users/theac/Downloads/images-gif/images-gif/9.gif")
		button = Button(self, bg="White", image=img16, borderwidth=0,
						highlightthickness=0, activebackground="White",command=lambda:self.process("9"))

		button.image = img16
		button.grid(row=2, column=2)


		self.pack(fill=BOTH, expand=1)






# processes button presses
	def process(self,button):
		#AC Clear the display
		if button =="AC" :
			# Clear the display
			self.display["text"] = ""
		# = starts an evalutation of whatever is on the display
		elif button == "=" :
			# get the expression on the display
			expr = self.display["text"]
			# the evalutation may return an error!
			try:
				# evaluate the expression
				result = eval(expr)
				self.display["text"] = str(result)
			# handle if an eror occurs during evaluation
			except:
			# note the error in the display
				self.display["text"] = "ERROR"
		# otherwise just tack on the appropriate operand / operator
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

