'''

In this notebook, we'll focus our discussion on the following problem:

QUESTION: Write a function to reverse a linked list

Before we answer this question, we need to answer:

What do we mean by linked list?
How do we create a linked list in Python?
How do we store numbers in a linked list?
How do we retrieve numbers in a linked list

## Linked List

A linked list is a _data structure_ used for storing a sequence of elements. It's data with some structure (the sequence).

![](https://cdn.programiz.com/sites/tutorial2program/files/linked-list-concept_0.png)

We'll implement linked lists which support the following operations:

- Create a list with given elements
- Display the elements in a list
- Find the number of elements in a list
- Retrieve the element at a given position
- Add or remove element(s)
- (can you think of any more?)


'''

"""class Node():
    def __init__(self) -> None:
        self.data = 0

node1 = Node()
node2 = Node()
node3 = node1
node4 = Node()


node1 = Node()
node1.data = 2 

node2 = Node()
node2.data = 3

node3 = Node()
node3.data = 5

print(node1.data,node2.data,node3.data)

"""
# Easier way to do it takes up less memory than above ^^^^^^^

class Node():
    def __init__(self, a_number) -> None:
        self.data = a_number
        self.next = None

    
node1 = Node(2)
node2 = Node(3)
node3 = Node(5)



### Linked List ###

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        
list1 = LinkedList()

list1.head  = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)

print(list1.head.data,list1.head.next.data,list1.head.next.next.data)
