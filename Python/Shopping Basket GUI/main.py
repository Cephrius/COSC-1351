from tkinter import *
from tkinter import messagebox

class ShoppingCartGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.item_list = [
            {"name": "Campbells Tomato Soup, 10oz Can", "image_path": "shoppingbasketphotos/417-4173228_can-of-campbells-tomato-soup-hd-png-download.png"},
            {"name": "Barrila Original Spaghetti,40oz", "image_path": "shoppingbasketphotos/a2e9d4e789c0f322a1cba28bf526bc75_99c73101-a5e2-4c36-bb8e-384825d62139_large.png"},
            {"name": "Kraft Macaroni and Cheese, 7.25oz Box", "image_path": "shoppingbasketphotos/242-2425390_mac-and-cheese-png-macaroni-and-cheese-box.png"},
            {"name": "Mountain Dew, 330ml Can", "image_path": "shoppingbasketphotos/487-4875579_mountain-dew-330ml-can-mountain-dew-330ml-hd.png"},
            {"name": "Amazon Prime Membership, Monthly", "image_path": "shoppingbasketphotos/download.png"},
            {"name": "Large Red Apples", "image_path": "shoppingbasketphotos/Large_Red_Apples_PNG_Clipart.png"}
        ]
        self.shopping_cart = {}
        self.items_sold = {}
        self.create_widgets()
    
    def create_widgets(self):
        self.master.config(bg="lightGrey")
        self.master.geometry("2000x700")
        self.master.resizable(False, False)
               
        # Create all of the Items to be sold
        for i, item in enumerate(self.item_list):
            img = PhotoImage(file=item["image_path"])
            item_label = Label(self.master, image=img)
            item_label.grid(row=1, column=i)
            
            space = Label(self.master, bg="lightGrey", width=11)
            space.grid(row=2, column=i)
            
            name_label = Label(self.master, text=item["name"])
            name_label.grid(row=3, column=i)
            
            space = Label(self.master, bg="lightGrey")
            space.grid(row=4, column=i)
            
            add_button = Button(self.master, text="Add to cart", command=lambda item=item: self.add_to_cart(item))
            add_button.grid(row=5, column=i)
            
        # Create cart display
        self.cart_label = Label(self.master, text="Shopping Cart", font=("Arial", 20), fg="white", bg="black", pady=5, padx=5)
        self.cart_label.grid(row=6, columnspan=6, sticky=W+E)
        
        self.clear_cart_button = Button(self.master, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.grid(row=6, column=6, sticky=E)
        
        self.cart_text = Text(self.master, width=60, height=20)
        self.cart_text.grid(row=7, columnspan=7)
        
        # Create checkout button
        self.checkout_button = Button(self.master, text="Checkout", bg="green", fg="white", font=("Arial", 20), command=self.checkout)
        self.checkout_button.grid(row=8, columnspan=7, pady=10)
        
    def add_to_cart(self, item):
        if item["name"] not in self.shopping_cart:
            self.shopping_cart[item["name"]] = 1
        else:
            self.shopping_cart[item["name"]] += 1

        self.update_cart_display()

    def update_cart_display(self):
        self.cart_text.delete("1.0", END)
        for item_name, item_quantity in self.shopping_cart.items():
            item_total_price = item_quantity * self.items_sold[item_name]["price"]
            self.cart_text.insert(END, f"{item_quantity}x {item_name} - ${item_total_price:.2f}\n")
        self.cart_text.insert(END, f"\nTotal Price: ${self.calculate_total_price():.2f}")

       
