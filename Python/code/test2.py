from tkinter import *

class ShoppingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping List")
        self.items = []

        # Create listbox to show items
        self.listbox = Listbox(self.master, width=50)
        self.listbox.pack(side=LEFT, padx=10, pady=10)

        # Create scrollbar for the listbox
        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=LEFT, fill=Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Create label and entry for adding new items
        self.label = Label(self.master, text="Add Item:")
        self.label.pack(pady=5)
        self.entry = Entry(self.master, width=30)
        self.entry.pack()

        # Create button for adding new items
        self.add_button = Button(self.master, text="Add", command=self.add_item)
        self.add_button.pack(pady=5)

        # Create button for removing selected item
        self.remove_button = Button(self.master, text="Remove", command=self.remove_item)
        self.remove_button.pack(pady=5)

        # Create button for clearing all items
        self.clear_button = Button(self.master, text="Clear", command=self.clear_items)
        self.clear_button.pack(pady=5)

    def add_item(self):
        item = self.entry.get()
        if item:
            self.items.append(item)
            self.listbox.insert(END, item)
            self.entry.delete(0, END)

    def remove_item(self):
        index = self.listbox.curselection()
        if index:
            self.listbox.delete(index)
            self.items.pop(index[0])

    def clear_items(self):
        self.listbox.delete(0, END)
        self.items.clear()

if __name__ == "__main__":
    root = Tk()
    shopping_gui = ShoppingGUI(root)
    root.mainloop()
