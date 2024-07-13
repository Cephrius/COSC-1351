#############################################

# Name: Chiedozie Ehileme                                                                                             

# Quiz Version: C                                                          

# Date:  FEBURARY 8, 2023                                                                                              

# Description: Implemented classes called resturant and IceCream                                                                                   

#############################################



class resturant():
    def __init__(self,resturant_name,cuisine_type) :
        self.resurant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"The name of this resturant is {self.resurant_name}")
        print(f"This resturant is an {self.cuisine_type} type resturant")

    def open_resturant(self,state):
        if state == "no" or state == "No":
            print(f"{self.resurant_name} is Not Open.")
            
        elif state == "yes" or state == "Yes":
            print(f"{self.resurant_name} is Open.")
        
        else:
            raise ValueError("NEEDS TO BE YES OR NO..")

    


class IceCreamStand(resturant):
    def __init__(self, resturant_name, cuisine_type,flavours):
        super().__init__(resturant_name, cuisine_type)
        self.flavours = flavours


    def showFlavours(self):
      list = []
      list.append(self.flavours)
      for flavour in list:
          print("################################################")
          print(f"FLAVOURS AVAILABLE at {self.resurant_name}")
          print(f"{flavour}")
          print("################################################")





########################## MAIN CODE ################################



r1 = resturant("John's Pizza","Pizza")
i1 = IceCreamStand("Ben and Jerry","Ice Cream","Strawberry, Vanilla")
i2 = IceCreamStand("PoP's Ice Cream","Ice Cream", "Caramel Swirl, Rainbow Pop")

r1.describe_resturant()
r1.open_resturant("Yes")

i1.open_resturant("Yes")
i1.describe_resturant()
i1.showFlavours()


i2.open_resturant("No")
i2.describe_resturant()
i2.showFlavours()


