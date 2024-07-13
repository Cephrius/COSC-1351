'''

################## 2D LISTS ################

drinks = ["Coffee","Soda","Water"]
dinner = ["Pasta","chicken","Carrots"]
dessert = ["Cake","Candy","Ice Cream"]

food = [drinks,dinner,dessert]

print(food[1][2])
'''

'''
################# TUPLES #######################
# tuple = collection which is ordered and unchangeable used
#         to group together related data

student = ("Bro",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here...")
'''
"""

#################### SETS ####################h
#set = collection which is unordered, unindexed. No duplicate values


utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
dinner_table = utensils.union(dishes)
dishes.update(utensils)

#Finds the differences in the lists when comparing
print(dishes.difference(utensils))

#Checks for anything that are common between the two
print(utensils.intersection(dishes))

#print(x)
"""

################ Dictionary #################
# Dictionary = A changable, unordedred collection of unique key: value pairs
#               Fast because they use hasting, allows to acces a value quickly




capitals = {'USA': 'Washigntion DC',
            'India': 'New Dehli',
            'China': 'Beiging',
            'Russia': 'Moscow'}

#print(capitals['Germany'])

# Checks if key is in dictionary
#print(capitals.get('Germany'))

#  Prints all of the keys in the dictionary
#print(capitals.keys())

# Print all of the values in the dictionary
#print(capitals.values())

# Prints the keys and their values together
#print(capitals.items())

# Prints the keys and their values in a for loop
#for key,values in capitals.items():
    #print(key,values)

# Updates a dictonary with a new key and value or an exisiting one 
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})

# Removes a key and its value
#capitals.pop('China')

# Clears entire dictionary
#capitals.clear()

for key,values in capitals.items():
    print(key,values)

'''
############## Not in keyword ##################################
color_list_1 = ['White','Black','Red','Blue']
color_list_2 = ['Red','Green','yellow']

color_list_3 = []
for element in color_list_2:
    if element not in color_list_1:
        color_list_3.append(element)
print("The differences are {}".format(color_list_3))
##############################################################
'''

'''  
def shout(string):
    return string.upper()

print(shout(input("Enter your name: ")))

yell = shout

print(yell("Hello"))
'''
"""
################ INDEXING ####################
 # index operator [] = gives access to a seqence's element (str,list,tuples)

name = "bro Code!"
 
#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
"""