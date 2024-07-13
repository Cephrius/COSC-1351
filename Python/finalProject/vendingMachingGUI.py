import sys
import subprocess
from tkinter import *


class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-fullscreen', True)
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.close_Window)
        
        # Create a Label widget
        self.label = Label(self.frame, text="")
        self.button = Button(self.frame,text ="",height=70, width=20,
                             font=("Comic Sans",100))
               

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def close_Window (self, event=None):
        self.tk.destroy()
        return "break"

class onScreen(Fullscreen_Window):
    
# run my C++ code
    def runCode(self):
        subprocess.run("")
    def __init__(self):
        super().__init__()
        
    def DispenseButton(self):
        # Update the text of the Label widget
       
        
        # get dimentions of the screen:
        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()
        
        x = (screen_width - self.button.winfo_reqwidth()) / 2 
        y = (screen_height - self.button.winfo_reqwidth()) / 2 
        
        self.button.config(text="DISPENSE", font=("Comic Sans", 200),bg="lightBlue",activebackground="lightBlue",command=self.runCode)
        self.button.pack(padx=y)
        
        
if __name__ == '__main__':
   
    # Call the DispenseButton method to display the label
    s = onScreen() #<----- Opens the window in fullscreen 
    s.DispenseButton() #<----- Calls the dispsenseButton function
    
    
    s.tk.mainloop()
