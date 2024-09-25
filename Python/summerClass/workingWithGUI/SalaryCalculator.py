from tkinter import *

# add comments to this code

class SalaryCalcuation(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        # Init the name label and Entry
        self.name_label = Label(window, text="Name: ", font=("Arial Bold", 24))
        self.name_label.grid(row=0, column=0, sticky=E)
        self.name_entry = Entry(window)
        self.name_entry.grid(row=0, column=1)

        # Init the salary label and entry
        self.salary_Label=Label(window, text="Montly Salary:", font=("Aerial Bold", 24), fg='red')
        self.salary_Label.grid(row=1, column=0, sticky='E')
        self.salary_entry = Entry(window)
        self.salary_entry.grid(row=1, column=1)

        # Calculate button
        self.calulate_button = Button(window, text="Calculate Annual Salary",
                                command=self.calculate_annual_salary, fg="blue",
                                font=("Arial Bold", 20), height=2)
        self.calulate_button.grid(row=2, column=0, columnspan=2)

        # init bouns
        self.bonus_var = IntVar()
        self.bonus = Checkbutton(window, text="With bonus 5%", variable=self.bonus_var)
        self.bonus.grid(row=3, column=1)

        # bonus scale
        self.bonus_scale = Scale(window, from_=0, to=20, orient=HORIZONTAL)
        self.bonus_scale.grid(row=4, column=1)


        # Result Label
        self.result_label = Label(window, text="", font=("Aerial Bold", 24))
        self.result_label.grid(row=5, column=0, columnspan=2)
        
    def calculate_annual_salary(self):
        """
        Calculates the annual salary based on the monthly salary entered by the user.

        This function retrieves the name and monthly salary from the user interface,
        multiplies the monthly salary by 12 to calculate the annual salary, and
        updates the result label with the calculated annual salary.
        """
        # Retrieve name and monthly salary from user interface
        name = self.name_entry.get()
        monthly_salary = float(self.salary_entry.get())

        # Calculate annual salary
        annual_salary = monthly_salary * 12 
        
        # Adding bonus
        if self.bonus_var.get() == 1:
            annual_salary=annual_salary * self.bonus_scale.get() # <---- get value from slider

        # Update result label with calculated annual salary and with commas for larger numbers
        self.result_label.config(text=f"Annual Salary: ${annual_salary:,}")
# Set the window 
window = Tk()
window.title("Salary Calculator")



app = SalaryCalcuation(window)
window.mainloop()


