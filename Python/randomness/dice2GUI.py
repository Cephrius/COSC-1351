from tkinter import *
from random import randint, seed

window = Tk()


dice_sums = [0] * 11





# Rolls 
Label1 = Label(window,text="Enter number of rolls",
                    font=("Comic Sans",10))

rolls = Entry(window,)

Label1.grid(row=0,column=0,sticky=W)
rolls.grid(row=0,column=1)

def roll():
    return randint(1,6)
    
for i in range(0, int(rolls.get())):
    die1 = roll()
    die2 = roll()

    dice_sum = die1 + die2
    dice_sums[dice_sum - 2] += 1

    print ("{}\t{}\t{}".format(die1, die2, dice_sum))

    # display a summary
print ("\nSum\tFreq\tProb")
for i in range(len(dice_sums)):
	print ("{}\t{}\t{}".format(i + 2, dice_sums[i], dice_sums[i] * 1.0 / sum(dice_sums)))
# rand_seed 
Label2 = Label(window,text="Enter a seed",
                    font=("Comic Sans",10))

seedEnter = Entry(window)
Label2.grid(row=1,column=0,sticky=W)
seedEnter.grid(row=1,column=1,)

# Submit button 

button = Button(window,text="Compute",command=roll)
button.grid(row=2,column=0)

# Pack all the widgets


seed(seedEnter.get())
print ("Die 1\tDie 2\tSum")





window.mainloop()