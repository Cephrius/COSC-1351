from tkinter import *


class RectangleCalculator(Frame):
    def __init__ (self, window):
        super().__init__(window)
        self.window = window
        self.window.title("Rectangle Calculator")
        self.window.geometry("400x400")

        # Label for length
        self.length_label = Label(window, text="Length: ", font=("Arial Bold", 24))
        self.length_label.grid(row=0, column=0, sticky=E)
        self.length_entry = Entry(window)
        self.length_entry.grid(row=0, column=1)

        # Label for width
        self.width_label = Label(window, text="Width: ", font=("Arial Bold", 24))
        self.width_label.grid(row=1, column=0, sticky=E)
        self.width_entry = Entry(window)
        self.width_entry.grid(row=1, column=1)

        # Calculate button
        self.calculate_button = Button(window, text="Calculate Area and Perimeter",
                                       command=self.calculate,
                                       font=("Arial Bold", 15), height=3, )
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        # Result Label
        self.result_label = Label(window, text="", font=("Arial Bold", 24))
        self.result_label.grid(row=3, column=0, columnspan=2)
        
    def calculate(self):
        
        length = self.length_entry.get()
        width = self.width_entry.get()
        area = int(length) * int(width)
        perimeter = 2 * (int(length) + int(width))
        self.result_label.config(text="Area: " + str(area) + "\nPerimeter: " + str(perimeter))
        
# set the window
window = Tk()
window.title("Rectangle Calculator")
window.geometry("600x300")
app = RectangleCalculator(window)
window.mainloop()
