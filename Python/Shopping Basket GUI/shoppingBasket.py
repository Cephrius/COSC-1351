class Item:
    # Constructor
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.original_stock = stock  # store the original stock value
        self._stock = stock

    @property
    def stockLevel(self):
        return self._stock

    @stockLevel.setter
    def stockLevel(self, value):
        if value < 0:
            raise ValueError("Stock level can not be negative")
        self._stock = int(value)

    def reset(self):
        self._stock = self.original_stock  # set the stock back to its original value


class ShoppingBasket(Item):
    # Constructor
    def __init__(self):
        self.items = []  # A dictionary of all the items in the shopping basket: {item:quantity}
        self.quantities = []
        self.checkout = False
        
    #A method to find and return the index of an item in the items list
    def findItem(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].name == item.name:
                return i
        return -1

    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=0):
        if quantity > 0:
            # Check if the item is already in the shopping basket
            index = self.findItem(item)
            
            if int(quantity) > item._stock:
                print(f"Not enough stock {item.name}")
                self.removeItem(item)

            
            else: 
                if index != -1:
                    self.quantities[index] += quantity
                 
                else:
                    self.items.append(item)
                    self.quantities.append(quantity)
            
            item._stock -= int(quantity)    
        else:
            print("Invalid operation - Quantity must be a positive number!")

       
    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item, quantity):
        if quantity > 0:
            index = self.findItem(item)
        if (index != -1):
            item.reset()
            self.quantities[index] = quantity
            item._stock += self.quantities[index] - quantity
            if int(quantity) > item._stock:
                print(f"Not enough stock {item.name}")
                item.reset()
                self.removeItem(item)
        else:
            self.removeItem(item)

    # A method to remove an item from the shopping basket (or reduce its quantity)
    def removeItem(self, item, quantity=None):
        index = self.findItem(item)
        if (index != -1):
            if quantity is None or quantity >= self.quantities[index]:
                # Remove the item entirely
                self.items.remove(item)
                del self.quantities[index]
                item._stock += self.quantities[index]
            elif quantity <= 0:
                raise ValueError("Invalid operation - Quantity must be a positive number!")
            else:
                # Reduce the quantity of the item
                self.quantities[index] -= quantity
                item._stock += quantity




    # A method to view/list the content of the basket.
    def view(self):
        totalCost = 0
        print("---------------------")
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = quantity * item.price
            print(" + " + item.name + " - " + str(quantity) + " x $" + '{0:.2f}'.format(
                item.price) + " = $" + '{0:.2f}'.format(cost))
            totalCost += cost
        print("---------------------")
        print(" = $" + '{0:.2f}'.format(totalCost))
        print("---------------------")
        


    # A method to calculate the total cost of the basket.

    def getTotalCost(self):
        totalCost = 0
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = quantity * item.price
            totalCost += cost
        return totalCost
    
    # A method to empty the content of the basket
    def reset(self):
        for item in self.items:
            item.reset()  # reset each item to its original stock value
        self.items.clear()
        self.quantities = []

    # A method to return whether the basket is empty or not:
    def isEmpty(self):
        return len(self.items) == 0
    


# Shopping Basket Class
tomatoSoup = Item("Tomato Soup", "200mL can", 0.70,100)
spaghetti = Item("Spaghetti", "500g pack", 1.10,200)
blackOlives = Item("Black Olives Jar", "200g Jar", 2.10,100)
mozarella = Item("Mozarella", "100g", 1.50,110)
gratedCheese = Item("Grated Cheese", "100g", 2.20,100)


myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)

myBasket.updateItem(tomatoSoup,100)
myBasket.removeItem(tomatoSoup,20)




myBasket.view()




