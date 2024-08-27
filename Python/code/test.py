class Item:
    # Constructor
    def __init__(self,name,description,price,stock):
        self.name = name
        self.description = description
        self.price = price
        self._stock = int(stock)
        
    @property
    def stockLevel(self):
        return self._stock
    
    @stockLevel.setter
    def stockLevel(self,value):
        if value < 0:
            raise ValueError("Stock level can not be negative")
        self._stock = int(value)


class ShoppingBasket(Item):
    # Constructor
    def __init__(self):
        self.items = []  # A list of all the items in the shopping basket
        self.quantities = []  # A list of all the quantities of each item
        self.checkout = False
    
    #A method to find and return the index of an item in the items list
    def findItem(self, item):
        for i in range(len(self.items)):
            if self.items[i].name == item.name:
                return i
        return -1
    
    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=0):
        if quantity <= 0:
            print("Invalid operation - Quantity must be a positive number!")
            return
        # Check if the item is already in the shopping basket
        index = self.findItem(item)
        if index != -1:
            self.quantities[index] += quantity
        else:
            self.items.append(item)
            self.quantities.append(quantity)
        item._stock -= quantity
    
    # A method to remove an item from the shopping basket (or reduce its quantity)
    def removeItem(self, item, quantity=0):
        index = self.findItem(item)
        if index != -1:
            if quantity <= 0 or quantity >= self.quantities[index]:
                # Remove the item completely
                self.items.pop(index)
                self.quantities.pop(index)
                item._stock += self.quantities[index]
            else:
                # Reduce the quantity of the item
                self.quantities[index] -= quantity
                item._stock += quantity
    
    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item, quantity):
        if quantity <= 0:
            self.removeItem(item)
        else:
            index = self.findItem(item)
            if index != -1:
                # Remove the item from the basket
                self.items.pop(index)
                self.quantities.pop(index)
            # Add the item back with the updated quantity
            self.addItem(item, quantity)
    
    # A method to view/list the content of the basket
    def view(self):
        totalCost = 0
        print("---------------------")
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = quantity * item.price
            print(" + " + item.name + " - " + str(quantity) + " x $" + '{0:.2f}'.format(item.price) + " = $" + '{0:.2f}'.format(cost))
            totalCost += cost
        print("---------------------")
        print(" = $" + '{0:.2f}'.format(totalCost))
        print("---------------------")
    
    # A method to calculate the total cost of the basket
    def getTotalCost(self):
        totalCost = 0
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = quantity * item.price
           
