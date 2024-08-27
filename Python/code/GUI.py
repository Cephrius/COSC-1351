
from tkinter import *
######################################
"""
window = Tk()
window.title("Making a Button")
window.geometry

b = Button(window,fg = 'Blue', 
           bg = 'Yellow', text= "Submit")
b.pack()
window.mainloop()
"""

####################################
"""
window = Tk()

l1 = Label(window,
           text="A Label",
            )
l1.grid(row = 0,
        column=0,
        sticky=E+S)

l2 = Label(window,
           text="Another Window")
l2.grid(row=1,
        column=0)

e1 = Entry(window)
e1.grid(row=0,
        column=1)

e2 = Entry(window)
e2.grid(row=1, 
        column=1)

window.mainloop()
"""

##########################################

class GUITest(Frame):
    def __init__ (self,master):
        Frame.__init__(self,master)
        self.master = master

   
    
    def setupGUI(self):
        l1 = Label(self.master,
                text="A Label")
        l1.grid(row=0,
                column=0,
                sticky=W
                )
        l2 = Label(self.master,
                text= "Another Label")
        l2.grid(row=1,
                column=0
                ,sticky=W)
        l3 = Label(self.master,
                text="A Thrid Label, centered")
        l3.grid(row=2,
                column=0,
                columnspan=2,
                sticky=E+W)
        
        frameCnt = 18
        frames = [PhotoImage(file='Python\sda.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]


        
        l4 = Label(self.master,
                   image=frames
                   )
        l4.image = frames
        
        l4.grid(row=0,
                column=2,
                columnspan=2,
                sticky=N+S+E+W
                )
                
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image = frame)
        window.after(100,update,ind)

label = Label(window)
label.pack()        
window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()