
from tkinter import *

###########################################################################################
# Name: Chiedozie Ehileme
# Date: Feburary 13, 2023
# Description: Creating a shopping class integrated into GUI for a more friendly apperance
# for the user.
###########################################################################################



class GUITest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        b1 = Button(self.master, text="Checkout", command=self.newWindow)
        b1.grid(row=0, column=0)

        b2 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\417-4173228_can-of-campbells-tomato-soup-hd-png-download.png")
      
        b3 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\242-2425390_mac-and-cheese-png-macaroni-and-cheese-box.png")

        b4 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\487-4875579_mountain-dew-330ml-can-mountain-dew-330ml-hd.png")

        b5 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\761-7612395_apple-png-image-download-apple-jpeg.png")

        b6 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\a2e9d4e789c0f322a1cba28bf526bc75_99c73101-a5e2-4c36-bb8e-384825d62139_large.png")

        b7 = PhotoImage(file="C:\\Users\\theac\\Documents\\Visual Code Programming\\COSC-1351-1\\Python\\shoppingbasketphotos\\download.png")

        label = Label(self.master, text="This is the main window")
        label.grid(row=1, column=0)

        label2 = Label(self.master,image=b2)
        label2.grid(row=0,column=1)


    def newWindow(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(self.master)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        l1 = Label(newWindow, text="This is a new window")
        l1.pack()

window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()
