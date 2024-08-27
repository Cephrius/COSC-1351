
class Dog:
    kind = "Canine"
    tricks = []
    def __init__(self,dog_breed,dog_name,dog_colour) -> None:
        self.breed = dog_breed
        self.name = dog_name
        self.colour = dog_colour
        self.tricks = []
        pass

    def __str__(self) -> str:
        return f'You have a {self.colour} {self.breed} named {self.name} and he can do the following tricks: {self.tricks}'
        pass
    
    def addTrick(self, trick):
        self.tricks.append(trick)

    
d1 = Dog("Goldennoodle","Adam","goldenBrown")
d1.addTrick("Bark")
print(d1)

'''   
tricks =[]
for i in range(0,1):
    print("Enter your Dog's info")
    colour = input("Enter you dog's colour: ")
    breed = input("Enter your dog's breed: ")
    name = input("Enter your dog's name: ")
    tricks = input("What trick can your dog do?")
'''



    