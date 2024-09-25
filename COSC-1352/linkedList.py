a=[]
for i in range(10):
    a.append(i)
print(a)
# /*************  ✨ Codeium Command 🌟  *************/
# create a linked list from a list
# the linked list is defined as a sequence of nodes
# each node has a data field and a link field
# the link field points to the next node in the sequence

class Node:
    def __init__(self,data=0,link=None):
        # data is the payload of the node
        # link is the reference to the next node in the sequence
        self.data=data
        self.link=link
        
# create the head of the linked list
a_head = a_tail=Node()

# loop over the list and add each element to the linked list
# the new node is added to the end of the list
for i in range(10):
    new_node=Node(i)
    a_tail.link = new_node
    a_tail = new_node

# print the linked list
current = a_head.link

while current is not None:
    print(current.data, end=", ")
    current = current.link

