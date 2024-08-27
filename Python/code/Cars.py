

class Car:
    def __init__(self, car_model,car_make,car_colour):
        self.model = car_model
        self.make = car_make
        self.colour = car_colour
        pass

    def __str__(self):
        return "You have a {} {} {} ".format(self.colour, self.make, self.model)
        pass
    
    def startCar(self):
        print("Go Car")
    
    def parkCar(self):
        print("Go to park")
    
    def evaluateCar(self):
        if(self.make == 'BMW'):
            print("This is a great car")
        elif(self.make == "Honda"):
            print("This is an OK car.")
        elif(self.make == 'VW'):
            print("They say its a bad car.")
        return None
        

# main

# Get user input for the car specs
carsList = []
for i in range(0,1):
    print("Enter your car specs")
    model = input("Enter the car model: ")
    make = input("Enter the car make: ")
    colour = input("Enter the car colour: ")

# Create the car object.
    cars1 = Car(model,make,colour)
    print(cars1)
# Add the car to our carList[] from above.
    carsList.append(cars1)
    print(carsList[i])

# Display list of cars
for i in range (0, len(carsList)):
    print('')
    print(carsList[i].evaluateCar())
    pass


'''
# instantiating objects of class car
c1 = Car('Model Y', 'Tesla', 'Blue') # First Object
c2 = Car('Civic', 'Honda','Red') # Second Object

print('First car is a {} and it is a {} and its {}'.format(c1.make  ,c1.model,c1.colour))
c1.colour = 'Blue'
print('First car is a {} and it is a {} and its {}'.format(c1.make,c1.model,c1.colour))
'''
