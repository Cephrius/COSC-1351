#####################################################################
# Name: Chiedozie Ehileme
# Date: March 9 2023
# Description: Your task is to implement the Room Adventure game with GUI improvements 
# above the text-based version of the game we programmed in COSC 1351. 
#####################################################################
import pygame
from tkinter import*

pygame.init()

class Room(object):
    # the constructors
    def __init__(self,name,image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []  
        

    # Getters and setters
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self,value):
        self._image = value

    @property
    def exits(self):
        return self._exits
    
    @exits.setter
    def exits(self,value):
        self._exits = value
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self,value):
        self._items = value
    
    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self,value):
        self._grabbables = value
    
    # adds exits to room the exit is a string (eg. north)
    # the room is an instance of a room
    
    def addExit(self,exit, room):
        # appened the exit and room to the appropriate dictornary

        self._exits[exit] = room

    # adds an item to the room the item is a string, the desc is a string that describes the items

    def addItem(self,item,desc):
        # append the item and description to the appropritate dictionary 
        self._items[item] = desc
    
    #adds grabbable item to the room 
    def addGrabbable(self,item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (eg, key)
    def delGrabbable(self,item):
        # remove the item from the list
        self._grabbables.remove(item)

    def delInventory(self,item):
        # remove item from list
        self._invetory.remove(item)

    # returns the string desciption
    def __str__(self):
        # first the room name
        s = f"You are in {self.name}\n"

        # next, the items in the room
        s += "You see: "
        
        for item in self.items.keys():
            s += item + "||"
        s += "\n"

        # items you can take
        e = f"You can take: {self.grabbables}\n"
        
        # next, the exits from the room
        s += "Exits: "

        for exit in self.exits.keys():
            s += exit + " "

        return s + "\n" + e

################## END OF CLASS DEF ################################

##################### MAIN PART OF GAME ############################

class Game(Frame):
    def __init__(self,parent):
        # call the constructor in the superclass
        Frame.__init__(self,parent)
    
    # creates the rooms
    def createRooms(self):
        # image in the current directory

        # living room
        r1 = Room("Living Room", "livingroom.png")
        # Kitchen
        r2 = Room("Kitchen","kitchen.png")
        # Homeoffice
        r3 = Room("Home Office","homeoffice.png")
        # bedroom
        r4 = Room("Bedroom","bedroom.png")
        # Dungeon / Basement
        r5 = Room("Basement","basement.png")

        # Add Exits to room
        r1.addExit("east", r2)
        r1.addExit("south", r3)

        # Add the Grabbable
        r1.addGrabbable("book")
        r1.addGrabbable("cup")
        r1.addGrabbable("coaster")
        r1.addGrabbable("vase")


        # add the items
        r1.addItem("sofa","a long upholstered seat with a back and arms, for seating several people")
        r1.addItem("chair", "A nice reclining chair")
        r1.addItem("table", "A broken table")
        r1.addItem("book","The book is George Orwell's Animal Farm")
        r1.addItem("television","an electronic device used for receiving broadcast signals and displaying images and sound")
    

        # Add room 2
        r2.addExit("west", r1)
        r2.addExit("south", r4)

        r2.addItem("rug", "A nice fancy persian rug")
        r2.addItem("gas stove", " the gas stove is not lit up")
        r2.addItem("refrigerator", " an appliance used for storing food and drinks at a low temperature")
        r2.addItem("mircowave","an appliance used for cooking or heating food using electromagnetic radiation")
        r2.addItem("blender","an appliance used for mixing and blending food and drink ingredients")

        r2.addGrabbable("cookie")
        r2.addGrabbable("bread")
        r2.addGrabbable("cup")
        r2.addGrabbable("plate")


        # Add room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addExit("south",r5)

        r3.addGrabbable("paperclip")
        r3.addGrabbable("key")
        r3.addGrabbable("laptop")
        r3.addGrabbable("staples")
        r3.addGrabbable("pen")

        r3.addItem("booksheleves", "It's a wall to wall bookshelf")
        r3.addItem("statue", "A statue of George Washignton")
        r3.addItem("computer","an electronic device used for processing and storing data")
        r3.addItem("lamp","an electric light with a shade or cover")

        # Add room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None)

        r4.addGrabbable("bottle")
        r4.addGrabbable("journal")
        r4.addGrabbable("towel")
        r4.addGrabbable("shoes")

        r4.addItem("alarm clock"," a clock used for waking up at a specific time")
        r4.addItem("mirror"," a reflective surface used for grooming and dressing.")
        r4.addItem("piano", "Yahmaha's 9 foot concert Grand Piano")
        r4.addItem("night stand","a small table or cabinet used for holding items next to a bed")


        # add room 5
        r5.addExit("north",r3)
        

        r5.addItem("car", "Your two Tesla's are in garage")
        r5.addItem('pool table', "Pool table to play pool with")
        r5.addItem("television", "an electronic device to watch various forms of entertainment on")

        r5.addGrabbable("cue")
        r5.addGrabbable("8-ball")
        r5.addGrabbable("carkeys")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []

    
    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill = BOTH, expand = 1)

        # setup the player input at the bottom of the GUI
        # the widget is a tkinter Entry
        # set its background to white and bind the return key to the function process in the class
        # push it to the bottom of the GUI and let it fill 
        # horizontally
        # give it focus so the player doesnt hae to click on it 
        
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>",self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # dont let the image control the widgets size
        img = None
        Game.image = Label(self,width=int(WIDTH/2), image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT,fill=Y)
        Game.image.pack_propagate(False)


        # setup the text to the right of the GUI
        # first the frame in which the text will be placed
        text_frame = Frame(self,width=WIDTH/2)
        
        # the widget is a tkinter text
        # disable is by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame,bg="lightgrey",state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT,fill=Y)
        text_frame.pack_propagate(False)
     
    # sets up the music for the GUI
    def setMusic(self):
        pygame.mixer.music.load("sound1.wav")
        pygame.mixer.music.play(-1)

    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room 
            Game.img = PhotoImage(file=Game.currentRoom.image)
        # display the image on the left of the GUI
        Game.image.config(image = Game.img)
        Game.image.image = Game.img


    # sets the status displayed on the right of the GUI
    def setStatus(self,status):
        # enable the text widget, clear it, set it and disable it
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            pygame.mixer.music.load("death.wav")
            pygame.mixer.music.play(-1)
            Game.text.insert(END, "You died jumping out the window. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status 
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n"+ status)
        Game.text.config(state = DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status 
        self.setStatus("")
        # set the audio
        self.setMusic()
    
    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()

        # set the user's input to lowercase to make it eaiser to compare the verb and noun to known values
        action = action.lower()

        # set a default respone
        response = "I dont understand. Try verb noun. Vaild verbs are go, look and take."

        #exit the game if the player wants to leave (supports quit,exit,and bye)
        if action == "quit" or action == "exit" or action == "bye" or action == "sionara!":
            exit(0)

        # if the player is dead if goes/went south from room 4 
        if Game.currentRoom == None:
            # clear the player input
            Game.player_input.delete(0,END)
            return
        
        # split the user input into words (words are seperated by spaces) and store the words in a list
        words = action.split()

        # if the game only understands two word inputs 
        if (len(words)  == 2): 
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if verb == "go":
                # set the default response
                response = "Invalid exit."
                # check for vaild exits in the current room 
                if noun in Game.currentRoom.exits:
                    # if one is found, change the current room to the one that is associated with the specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    # set tge response (success) 
                    response = "Room Changed."
            # the verb is look
            elif verb == "look":
                # set a deafualt response 
                response = "I don't see that item."

                # check for vaild items in the current room
                if noun in Game.currentRoom.items:
                    # if one is found, set the response to the item's description 
                    response = Game.currentRoom.items[noun]
                    
                    # the verb is take
            elif (verb == "take"):
                # set a default response
                response = "I dont see that item."
                
                # check for vaild grabbable items in the current room 
                for grabbable in Game.currentRoom.grabbables:
                    # a vaild grabblabe item is found 
                    if (noun == grabbable):
                        # add the grabble item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabblable item from the room 
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response(success)
                        response = f"You grabbed the {noun}."
                        # no need to check any more grabbable items
                        break
            # the verb is drop
            elif verb == "drop":
                # set default response
                response = "You didnt pick up that item"
                # a valid item is found
                for grabbable in Game.inventory:
                    if noun == grabbable:
                        Game.inventory.remove(noun)
                        # add item back to grabbable list
                        Game.currentRoom.addGrabbable(noun)
                        # set response (success)
                        response = f"You dropped the {noun}"
                        break
                
                
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)
                    


def death():
    print (" " * 17 + "u" * 7)
    print (" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print (" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print (" " * 9 + "u" + "$" * 21 + "u")
    print (" " * 8 + "u" + "$" * 23 + "u")
    print (" " * 7 + "u" + "$" * 25 + "u")
    print (" " * 7 + "u" + "$" * 25 + "u")
    print (" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3
    + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print (" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " *
    7 + "$" * 4 + "\"")
    print (" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u"
    + "$" * 3)
    print (" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" +
    " " * 6 + "u" + "$" * 3)
    print (" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +
    "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print (" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" *
    7 + "\"")
    print (" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print (" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print (" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" +
    "$" * 2 + " " * 7 + "u" * 3)
    print (" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 +
    " " * 7 + "u" + "$" * 4)
    print (" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +
    "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print ("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +
    "u" * 4 + "$" * 10)
    print ("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" *
    2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print (" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2
    + " " + "\"" * 2 + "$" + "\"" * 3)
    print (" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print (" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + "\"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print (" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *
    11 + "\"")
    print (" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$"
    * 4 + "\"\"")
    20
    print (" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")

"""

# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game


# play forever (well, at least until the player dies or asks to quit)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom,inventory)

# if the current room is None, then the player is dead
# this only happens if the player goes south when in room 4
    if (currentRoom == None):
        status = "You are dead."
        death()
    # display the status
    print ("=====================================================")
    print (status)

    # if the current room is None (and the player is dead), exit the
    # game
    if (currentRoom == None):

        break


# prompt for player input
# the game supports a simple language of <verb> <noun>
# valid verbs are go, look, and take
# valid nouns depend on the verb
# we use raw_input here to treat the input as a string instead of
# a numeric value
    action = str(input("What to do? "))

# set the user's input to lowercase to make it easier to compare
# the verb and noun to known values
    action = action.lower()

# exit the game if the player wants to leave (supports quit,
# exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break

# set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

# split the user input into words (words are separated by spaces)
    words = action.split()

# the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):

            # a valid exit is found
                if (noun == currentRoom.exits[i]):
            # change the current room to the one that is
            # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
            # set the response (success)
                    response = "Room changed."

            # no need to check any more exits
                    break

        # the verb is: look
        elif (verb == "look"):
        # set a default response
            response = "I don't see that item."
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found

                if (noun == currentRoom.items[i]):

                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break

        # the verb is: take
        elif (verb == "take"):

            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's
                    # inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable items
                    break

# display the response
print (f"\n{response}")


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!



 
"""


######################################################################
# The default size of the GUI is 800x600
WIDTH = 950
HEIGHT = 600

# create the window
window = Tk()

window.title("Room Adventure")


# Create the GUI as Tkinter canvas inside the window
g = Game(window)
# Play the game
g.play()


# wait for the window to close
window.mainloop()
