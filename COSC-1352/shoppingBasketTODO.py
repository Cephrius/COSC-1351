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
    
    
        for i in range(len(self.items)):
            if item.name == self.items[i].name:
                return i 
        return -1
        
        
    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=1):
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
        
        index = self.findItem(item) # <--- Returns the items index here using the function findItem
        if index != -1: # <---- if the item is in the array
            if quantity <= 0 or quantity >= self.quantities[index]: # <---- if the quantity is equal to the item.quantity then remove the whole item.
                # Remove the item entirely
                self.items.remove(item)
                del self.quantities[index]
            elif quantity <= 0:
                raise ValueError("Invalid operation - Quantity must be a positive number!")
            else:
                # Reduce the quantity of the item
                self.quantities[index] -= quantity
                

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

    # A method to view/list the content of the basket
    def view(self):
        totalCost = 0
        totalTax = 0
        print("---------------------")
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            tax = abs((item.price * item.tax/100) - item.price)
            cost = quantity * item.price
            print(f" + {item.name:20s} - {quantity:4d} x ${cost: 5.2f} + ${tax:5.2f} = ${cost:6.2f}")
            print(f"   ({item.description})")
            totalCost += cost
            subtotal = totalCost - totalTax
            totalTax += tax
        
        print("---------------------")
        print(f" Subtotal: ${subtotal:7.2f}")
        print(f" Tax:      ${totalTax:7.2f}")
        print(f" Total:    ${totalCost:7.2f}")
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
        for i in range(len(self.items)):
            pass

class Item:
    # Constructor
    def __init__(self, name, description, price,tax, year, month, day):
        self.name = name
        self.description = description
        self.price = price # price subtotal
        self.tax = tax #tax percentage
        self.exprireYear = year
        self.exprireMonth = month
        self.exprireDay = day
        

# ======================
# Test Code
# ======================

# Create some items
tomatoSoup = Item("Tomato Soup", "200mL can", 0.70,5)
spaghetti = Item("Spaghetti", "500g pack", 1.10,3)
blackOlives = Item("Black Olives Jar", "200g Jar", 2.10,3)
mozarella = Item("Mozarella", "100g", 1.50,3)
gratedCheese = Item("Grated Cheese", "100g", 2.20,3)
oreos = Item("Oreos", "1lb pack", 3.49,3)

# Create a ShoppingBasket instance
myBasket = ShoppingBasket()

# Perform operations on the basket
myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives)
myBasket.addItem(spaghetti, 5)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)
myBasket.addItem(oreos, 3)



# View the basket contents
myBasket.view()
print("\n\nThe total items cost in your basket is $", myBasket.getTotalCost())
