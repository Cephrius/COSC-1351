from tkinter import *


# create function to calculate area and perimeter
def calculate_area_perimeter():
    length = length_entry.get()
    width = width_entry.get()
    area = int(length) * int(width)
    perimeter = 2 * (int(length) + int(width))
    result_label1.config(text="Area: " + str(area))
    result_label2.config(text="Perimeter: " + str(perimeter))
    

# Create a new window
window = Tk()
window.geometry('600x300')
window.title("Rectangle Calculator")


# Add lables and Entry Widgets for Input
length_label = Label(window, text="Length")
length_label.config( text="Length: ", font=("Aerial Bold", 24))
length_label.pack()

length_entry = Entry(window)
length_entry.pack()

width_label = Label(window, text="Width")
width_label.config( text="Width: ", font=("Aerial Bold", 24))
width_label.pack()

width_entry = Entry(window)
width_entry.pack()


# Create Calculate button
calculate_button = Button(window, text="Calculate Area & Perimieter", command=calculate_area_perimeter )
calculate_button.pack()

# Add lable to display results
result_label1 = Label(window, text="", font=("Aerial Bold", 24))
result_label1.pack()

result_label2 = Label(window, text="", font=("Aerial Bold", 24))
result_label2.pack()

# Run the main loop
window.mainloop()



