from tkinter import *

class ShoppingCartGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
        
        
    
        self.tomatoPhoto = PhotoImage("/COSC-1351/Python/Shopping Basket GUI/shoppingbasketphotos/soup.png")
        self.tomatolabel = Label(self.master,image = self.tomatoPhoto)
        
        self.storeAmountPhoto =  PhotoImage("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\Python\\Shopping Basket GUI\\shoppingbasketphotos\\png-transparent-supermarket-shopping-basket-cartoon-shopping-basket-shopping-basket-illustration-supermarket-thumbnail.png")
        self.storeCheckLabel = Label(self.master,image=self.storeAmountPhoto)
        
        self.spaghettiPhoto = PhotoImage("C:/Users/theac/OneDrive/Documents/COSC-1351/Python/shoppingbasketphotos/a2e9d4e789c0f322a1cba28bf526bc75_99c73101-a5e2-4c36-bb8e-384825d62139_large.png")
        self.spaghettiLabel = Label(self.master, image= self.spaghettiPhoto)
        
        self.macandcheesephoto = PhotoImage("C:/Users/theac/OneDrive/Documents/COSC-1351/Python/shoppingbasketphotos/242-2425390_mac-and-cheese-png-macaroni-and-cheese-box.png")
        self.macandcheeselabel = Label(self.master, image= self.macandcheesephoto)
        
        self.mountiandewPhoto = PhotoImage("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\Python\\Shopping Basket GUI\\shoppingbasketphotos\\487-4875579_mountain-dew-330ml-can-mountain-dew-330ml-hd.png" )
        self.mountiandewLabel = Label(self.master,image=self.mountiandewPhoto)
        
        self.primePhoto = PhotoImage("C:/Users/theac/OneDrive/Documents/COSC-1351/Python/shoppingbasketphotos/download.png")
        self.primeLabel = Label(self.master, image=self.primePhoto)
    
        self.applesPhoto = PhotoImage("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\Python\\Shopping Basket GUI\\shoppingbasketphotos\\Large_Red_Apples_PNG_Clipart.png")
        self.applesLabel = Label(self.master, image=self.applesPhoto)
        
        
         # Create buttons
        
        
    
    def setupGUI(self):
        
        self.master.config(bg="lightGrey")     
        self.master.geometry("2000x700")
        window.resizable(False,False)
        
               
               
###############      
# Setup the shop
        ####################################
        # Create all of the Items to be sold
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="20")
        space.config(height="5")
        space.grid(row=0,column=0)
        
        b1 = Button(self.master,image=self.storeAmountPhoto,command = self.newWindow)
        b1.grid(row=1,column=12,sticky=N,)
        
        b2 = Label(self.master,image = self.tomatoPhoto)
        b2.grid(row=1,column=0)
         
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=1)
        
        b3 = Label(self.master,text= "Store",image = self.spaghettiPhoto)
        b3.grid(row=1,column=2)
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=3)
         
        b4 = Label(self.master,image=self.macandcheesephoto)
        b4.grid(row=1,column=4)
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=5)
        
        b5 = Label(self.master,image=self.mountiandewPhoto)
        b5.grid(row=1,column=6)
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=7)
        
        b6 = Label(self.master,image=self.primePhoto)
        b6.grid(row=1,column=8)
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=9)
        
        b7 = Label(self.master,image=self.applesPhoto)
        b7.grid(row=1,column=10)
        
        space = Label(self.master,bg="lightGrey")
        space.config(width="11")
        space.grid(row=1,column=11)
        
        ####################################
        # Create text for items sold
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=0)
        
        t1 = Label(self.master,text="Campbells Tomato Soup, 10oz Can")
        t1.grid(row=3,column=0)
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=1)
        
        t2 = Label(self.master,text="Barrila Original Spaghetti,40oz")
        t2.grid(row=3,column=2)
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=3)
        
        t3 = Label(self.master,text="Craft Macaroni & Cheese Dinner")
        t3.grid(row=3,column=4)
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=5)
        
        t4 = Label(self.master,text="Mountain Dew 8oz Can")
        t4.grid(row=3,column=6)
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=7)
        
        t5 = Label(self.master,text="Prime 'Blue Raspberry' Hydration Drink 12oz")
        t5.grid(row=3,column=8)
        
        
        space = Label(self.master,bg="lightGrey")
        space.grid(row=1,column=9)
    
        t6 = Label(self.master,text="Fresh Gala Apples ")
        t6.grid(row=3,column=10)
        
        
        ########################## 
        # Create purchase Entries
        
        itemEntry1 = Entry(self.master)
        itemEntry1.grid(row=4,column=0)
        
        itemEntry2 = Entry(self.master)
        itemEntry2.grid(row=4,column=2)
        
        itemEntry3 = Entry(self.master)
        itemEntry3.grid(row=4,column=4)
        
        itemEntry4 = Entry(self.master)
        itemEntry4.grid(row=4,column=6)
        
        itemEntry5 = Entry(self.master)
        itemEntry5.grid(row=4,column=8)
        
        itemEntry6 = Entry(self.master)
        itemEntry6.grid(row=4,column=10)
        
        #############################
        # Create Buttons for adding to cart
        
        
        itemAdd1 = Button(self.master,text="Add to cart")
        itemAdd1.grid(row=5,column=0)
        
        itemAdd2 = Button(self.master,text="Add to cart")
        itemAdd2.grid(row=5,column=2)
        
        itemAdd3 = Button(self.master,text="Add to cart")
        itemAdd3.grid(row=5,column=4)
        
        itemAdd4 = Button(self.master,text="Add to cart")
        itemAdd4.grid(row=5,column=6)
        
        itemAdd5 = Button(self.master,text="Add to cart")
        itemAdd5.grid(row=5,column=8)
        
        itemAdd6 = Button(self.master,text="Add to cart")
        itemAdd6.grid(row=5,column=10)

        

        


    
        
    def newWindow(self): # <---- serves as Checkout section for the store
            icon = PhotoImage(file="C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\Python\\shoppingbasketphotos\\png-transparent-supermarket-shopping-basket-cartoon-shopping-basket-shopping-basket-illustration-supermarket-thumbnail.png")
            
            # Toplevel object which will
            # be treated as a new window

            newWindow = Toplevel(self.master)
            newWindow.config(bg="lightGrey")
            newWindow.iconphoto(True,icon)
            newWindow.geometry("800x600")

            # sets the title of the
            # Toplevel widget
            newWindow.title("Checkout")

             # Create listbox to show items
            self.listbox = Listbox(newWindow, width=100)
            self.listbox.pack(side=LEFT, padx=10, pady=10)

            # Create scrollbar for the listbox
            scrollbar = Scrollbar(newWindow)
            scrollbar.pack(side=LEFT, fill=Y)
            self.listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.listbox.yview)


            # Create button for removing selected item
            self.remove_button = Button(newWindow, text="Remove", command=self.remove_item)
            self.remove_button.pack(pady=5)

            # Create button for clearing all items
            self.clear_button = Button(newWindow, text="Clear", command=self.clear_items)
            self.clear_button.pack(pady=5)
                
      
      
      
    

window = Tk()
t = ShoppingCartGUI(window)
t.setupGUI()
window.mainloop()
