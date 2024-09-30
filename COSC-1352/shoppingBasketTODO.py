

class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = []      # A list of all the items in the shopping basket
        self.quantities = [] # A list of the quantities corresponding to each item found in the items list
        self.checkout = False

    # A method to find and return the index of an item in the items list
    def findItem(self, item):

    # TODO: Implement this method
    # Iterate over the items list and return the index if the item is found.
    # Compare items based on their name attribute.
    # If the item is not found, return -1.
    # If the item is found, return the index.
        if isinstance(item, str):
            for i in range(len(self.items)):
                if self.items[i].name == item:
                    return i
        # If the input is an Item object, search by item.name
        elif isinstance(item, Item):
            for i in range(len(self.items)):
                if self.items[i].name == item.name:
                    return i

        return -1  # Item not found
        
    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=1):
        loyaltyPoints = 0
        # TODO: Implement this method
        # If quantity > 0:
        #   - Check if the item is already in the shopping basket using findItem.
        #   - If it exists, increase its quantity.
        #   - If not, append the item and its quantity to the lists.
        # Else:
        #   - Print an error message indicating that quantity must be positive.
        
        if quantity > 0:
            index = self.findItem(item) # -- Check if the item is in the shopping basket using findItem
            if index != -1:
                self.quantities[index] += quantity # -- Adding the extra quantity since it is in the basket already
            else:
                self.items.append(item)
                self.quantities.append(quantity)
                
        else:
            print("Error: Quantity must be positive.")
        

    # A method to remove an item from the shopping basket (or reduce its quantity)
    # e.g., removeItem(someItem) removes the item completely
    #       removeItem(someItem, 4) removes 4 pieces of the item
    def removeItem(self, item, quantity=0):
        # TODO: Implement this method
        # Find the item's index using findItem.
        # If the item exists:
        #   - If quantity <= 0:
        #       - Remove the item completely using del and index.
        #   - Elif the current quantity is greater than or equal to the quantity to remove:
        #       - Update the item's quantity by reducing it accordingly.
        
        # index = self.findItem(item) # <--- Returns the items index here using the function findItem
        # if index != -1: # <---- if the item is in the array
        #     if quantity <= 0 or quantity >= self.quantities[index]: # <---- if the quantity is equal to the item.quantity then remove the whole item.
        #         # Remove the item entirely
        #         self.items.remove(item)
        #         del self.quantities[index]
        #     elif quantity <= 0:
        #         raise ValueError("Invalid operation - Quantity must be a positive number!")
        #     else:
        #         # Reduce the quantity of the item
        #         self.quantities[index] -= quantity
                
        # item can now be either a string (name) or an Item object
        index = self.findItem(item)  # Works with item name or object
        if index != -1:
            if quantity <= 0 or quantity >= self.quantities[index]:
                # Remove the item entirely
                del self.items[index]
                del self.quantities[index]
            elif quantity <= 0:
                raise ValueError("Invalid operation - Quantity must be a positive number!")
            else:
                # Reduce the quantity of the item
                self.quantities[index] -= quantity
        else:
            print(f"Error: {item} not found in the basket.")

    # A method to update the quantity of an item in the shopping basket to the given value
    def updateItem(self, item, quantity):
        # TODO: Implement this method
        # Find the item's index using findItem.
        # If the item exists:
        #   - If quantity > 0:
        #       - Update the quantity to the new value.
        #   - Else:
        #       - Remove the item completely using removeItem.
        
        index = self.findItem(item)
        if index != -1:
            if quantity > 0:
                self.quantities[index] = quantity
            else:
                self.removeItem(item)
        pass
    
    # A method to return that allows items to be returned

    def returnItem(self, item_name, quantity):
        # # when item is returned then decrease the quantity in the shopping cart
        # # decrease the quanitity by the amount given 
        # index = self.findItem(items.name)  # item_name is a string

        # # If the item exists in the basket
        # if index != -1:
        #     if quantity <= 0:
        #         raise ValueError("Invalid operation - Quantity must be a positive number!")

        #     # Check if the return quantity is valid
        #     if self.quantities[index] >= quantity:
        #         self.quantities[index] -= quantity  # Reduce the quantity of the item

        #         # If the quantity becomes 0, remove the item from the basket
        #         if self.quantities[index] == 0:
        #             self.removeItem(items)
        #             del self.quantities[index]

        #         print(f"Returned {quantity} of {items.name}.")
        #     else:
        #         print(f"Error: Cannot return more than {self.quantities[index]} of {items.name}.")
        # else:
        #     print(f"Error: {items.name} is not in the basket.")
        
        # Find the item index using findItem (handles string names now)
        index = self.findItem(item_name)

        if index != -1:
            if quantity <= 0:
                raise ValueError("Invalid operation - Quantity must be a positive number!")

            # Check if the return quantity is valid
            if self.quantities[index] >= quantity:
                self.quantities[index] -= quantity  # Reduce the quantity

                # If the quantity becomes 0, remove the item from the basket
                if self.quantities[index] == 0:
                    del self.items[index]
                    del self.quantities[index]

                print(f"Returned {quantity} of {item_name}.")
            else:
                print(f"Error: Cannot return more than {self.quantities[index]} of {item_name}.")
        else:
            print(f"Error: {item_name} is not in the basket.")
        
        
    # A method to view/list the content of the basket
    def view(self):
        totalCost = 0
        totalTax = 0
        totalPoints = 0 
        subtotal = 0  # Initialize subtotal here
        print("---------------------")
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            tax = abs((item.price * item.tax/100) - item.price)
            cost = quantity * item.price
            totalPoints += item.loyaltyPoints * quantity
            print(f" + {item.name:20s} - {quantity:4d} x ${item.price: 5.2f} + ${tax:5.2f} = ${cost:6.2f}")
            print(f"   ({item.description})")
            totalCost += cost
            totalTax += tax
            subtotal = totalCost - totalTax  # Move this line outside the loop
            
        print("---------------------")
        print(f" Subtotal: ${subtotal:7.2f}")
        print(f" Tax:      ${totalTax:7.2f}")
        print(f" Total:    ${totalCost:7.2f}")
        print("-----------------------")
        print(f" Total points earned today: {totalPoints}")
        print("---------------------")

    # A method to calculate the total cost of the basket
    def getTotalCost(self):
        # TODO: Implement this method
        # Calculate the total cost by summing up the cost of each item (price * quantity).
        # Return the total cost
        self.checkout = True
        totalCost = 0
        for i in range(len(self.items)):
            tax = self.items[i].price + (self.items[i].price * (self.items[i].tax / 100))
            totalCost += (self.items[i].price * self.quantities[i])
        return totalCost


    # A method to empty the content of the basket
    def reset(self):
        # TODO: Implement this method
        # Clear the items and quantities lists.
        
        for i in range(len(self.items)):
            self.items = []
            self.quantities = []

    # A method to return whether the basket is empty or not
    def isEmpty(self):
        # TODO: Implement this method
        # Return True if the basket is empty, else False.
        for i in range(len(self.items)):
            if self.items[i] == 0:
                return True
            else: 
                return False
            
    # A method to fileter items based on their expiry date
    def filterItemByExpriry(self, year, month, day):
        # TODO: Implement this method
        # Filter the items in the basket based on their expiry date.
        # Return the filtered items.

        filteredItems = []
        print(f"Items expiring before {year}-{month:02d}-{day:02d}: \n")
        
        for i in range(len(self.items)):
            item = self.items[i]
            
            # Compare year, month, day manually
            if (item.expireYear < year or
                (item.expireYear == year and item.expireMonth < month) or
                (item.expireYear == year and item.expireMonth == month and item.expireDay < day)):
                filteredItems.append(item)
                print(f"{item.name} (expires on {item.expireYear}-{item.expireMonth:02d}-{item.expireDay:02d})")
        
        if len(filteredItems) == 0:
            print("No items are expiring before the specified date.")
        
        return filteredItems

        
        

class Item:
    # Constructor
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price # price subtotal
        self.tax = 0 #tax percentage
        self.expireYear = 0
        self.expireMonth = 0
        self.expireDay = 0
        self.loyaltyPoints = 0

# ======================
# Test Code
# ======================

# Create some items
# tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, 5, 2024, 12, 31, 4)
# spaghetti = Item("Spaghetti", "500g pack", 1.10, 3, 2024, 11, 15, 4)
# blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, 3, 2024, 10, 10, 4)
# mozarella = Item("Mozarella", "100g", 1.50, 3, 2024, 9, 30, 4)
# oreos = Item("Oreos", "1lb pack", 3.49, 3, 2025, 2, 1, 4)

# # Create a ShoppingBasket instance
# myBasket = ShoppingBasket()

# # Perform operations on the basket
# myBasket.addItem(tomatoSoup, 4)
# myBasket.addItem(blackOlives)
# myBasket.addItem(spaghetti, 5)
# myBasket.addItem(mozarella, 2)
# myBasket.addItem(tomatoSoup, 6)
# myBasket.addItem(oreos, 3)
# myBasket.returnItem(oreos)


#########################
# TESTER CODE 
##########################

def display_menu():
    print("\nShopping Basket Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item Quantity")
    print("4. View Cart")
    print("5 Filter Items by Expiry Date")
    print("6. Return Item")
    print("7. Exit")


def main():
    myBasket = ShoppingBasket()
    
    while True:
        display_menu()
        choice = input("Please choose an option: ")
        
        if choice == "1":
            # Add item
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            points = int(input("Enter item loyalty points: "))
            quantity = int(input("Enter item quantity: "))
            tax = float(input("Enter item tax percentange: "))
            year = int(input("Enter item expiry year: "))
            month = int(input("Enter item expiry month: "))
            day = int(input("Enter item expiry day: "))
            item = Item(name, description, price)
            item.loyaltyPoints = points
            item.tax = tax
            item.expireYear = year
            item.expireMonth = month
            item.expireDay = day
            myBasket.addItem(item, quantity)
            print(f"\n {name} added to basket")
            
        elif choice == '2':
            # Remove Item
            item_name = input("Enter the name of item to remove:")
            quantity = input("Enter the quantity to remove (leave blank to remove all): ")
            if quantity == '':
                myBasket.removeItem(item_name)
            else:
                quantity = int(quantity)
                myBasket.removeItem(item_name, quantity)
                
        elif choice == "3":
            # Update Item quantity
            item_name = input("Enter the name of the item to update: ")
            quantity = int(input("Enter the new quantity: "))
            myBasket.updateItem(item_name, quantity)
            
        elif choice == "4":
            # View Cart
            myBasket.view()
            
        elif choice == '5':
            # Filter Items by Expiry Date
            year = int(input("Enter the expiry year to filter by: "))
            month = int(input("Enter the expiry month to filter by: "))
            day = int(input("Enter the expiry day to filter by: "))
            myBasket.filterItemsByExpiry(year, month, day)
            
        elif choice == '6':
            # Return Item
            item_name = input("Enter the name of the item to return: ")
            quantity = int(input("Enter the quantity to return: "))
            myBasket.returnItem(item_name, quantity)
            
        elif choice == '7':
            # Exit
            break
            print("Exiting the shopping basket program.")
            
        else:
            print("Invalid option. Please choose a number between 1 and 7.")

# View the basket contents
main()


