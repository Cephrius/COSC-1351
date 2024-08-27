from tkinter import *

# add comments to this code


def calculate_annual_salary():
    """
    Calculates the annual salary based on the monthly salary entered by the user.

    This function retrieves the name and monthly salary from the user interface,
    multiplies the monthly salary by 12 to calculate the annual salary, and
    updates the result label with the calculated annual salary.
    """
    # Retrieve name and monthly salary from user interface
    name = name_entry.get()
    monthly_salary = float(salary_entry.get())

    # Calculate annual salary
    annual_salary = monthly_salary * 12 
    
    # Adding bonus
    if bonus_var.get() == 1:
        annual_salary=annual_salary*bonus_scale.get() # <---- get value from slider

    # Update result label with calculated annual salary and with commas for larger numbers
    result_label.config(text=f"Annual Salary: ${annual_salary:,}")
# Set the window 
window = Tk()
window.geometry('600x300')
window.title("Salary Calculator")

# Init the name label and Entry
name_label = Label(window, text="Name: ", font=("Arial Bold", 24))
name_label.grid(row=0, column=0, sticky=E)
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

# Init the salary label and entry
salary_Label=Label(window, text="Montly Salary:", font=("Aerial Bold", 24), fg='red')
salary_Label.grid(row=1, column=0, sticky='E')
salary_entry = Entry(window)
salary_entry.grid(row=1, column=1)

# Calculate button
calulate_button = Button(window, text="Calculate Annual Salary",
                         command=calculate_annual_salary, fg="blue",
                         font=("Arial Bold", 20), height=2)
calulate_button.grid(row=2, column=0, columnspan=2)

# init bouns
bonus_var = IntVar()
bonus = Checkbutton(window, text="With bonus 5%", variable=bonus_var)
bonus.grid(row=3, column=1)

# bonus scale
bonus_scale = Scale(window, from_=0, to=20, orient=HORIZONTAL)
bonus_scale.grid(row=4, column=1)


# Result Label
result_label = Label(window, text="", font=("Aerial Bold", 24))
result_label.grid(row=5, column=0, columnspan=2)

window.mainloop()


