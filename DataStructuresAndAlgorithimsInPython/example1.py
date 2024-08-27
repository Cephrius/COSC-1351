# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
# and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number 
# by turning over as few cards as possible. Write a function to help Bob locate the card.
import jovian
 
def locate_card(cards,query):
    # create a variable position with te value 0
    position = 0 
    
    # set up a loop for repetition 
    while position < len(cards):
        
        # check if the element at the current position mathces the query
        if cards[position] == query:
             
             # return position
             return position
        
        # Increment the position 
        position += 1
        
    #Number not found, return -1
    return -1
        




