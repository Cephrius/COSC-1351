from cgi import print_arguments
import math

'''
bottles = 99 

while (bottles > 0):
    print("{} bottles of beer on the wall".format(bottles))
    print("bottles of beer".format(bottles))
    print("Take one down, pass it around")
    bottles -= 1
    print(" {} bottles of beer on the wall".format(bottles))
    print()
'''

"""
def drinkBeer(bottles):
    if(bottles > 0):
        print("{} bottles of beer on the wall".format(bottles))
        print("bottles of beer".format(bottles))
        print("Take one down, pass it around")
        print(" {} bottles of beer on the wall".format(bottles))
        print()
        drinkBeer(bottles -1)

drinkBeer(99)
"""
"""
def drinkBeer(bottles):
    if(bottles > 0):
        print("{} bottles of beer on the wall".format(bottles))
        print("bottles of beer".format(bottles))
        print("Take one down, pass it around")
        bottles -=1 
        print(" {} bottles of beer on the wall".format(bottles))
        print()
        drinkBeer(bottles)
        print("Going Back")

drinkBeer(99)
"""

'''
# Working with Arrays
grades = [10,24,28,58,11,29]
print(grades)

listSize = len(grades)
print("The list size is {}".format(listSize))

largest = max(grades)
smallest = min(grades)

print("The Largest grade is {}".format(largest))
print("The smallest grade is {}".format(smallest))

grades.append(0)
print(grades)

c = grades.count(10)
print(str(c) + " studdents have the number 10")

grades.reverse()
print(grades)

grades.sort()
print(grades)

grades.remove(grades[2])
print(grades)

grades.insert(2,10)
print(grades)

print(grades.index(29))
'''
names = ["Neto","Brianna","Luis","David","John",10]

size = len(names)

for i in range (0,size):
    print(names[i])


"""
# Binary Tree example
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)2

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

print("Root Node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftChild.data)

print("right child of the node is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("right child of the node is:")
print(node2.rightChild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftChild)

print("right child of the node is:")
print(node4.rightChild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftChild)

print("right child of the node is:")
print(node5.rightChild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftChild)

print("right child of the node is:")
print(node6.rightChild)

print("Node is:")
print(node7.data)

print("left child of the node is:")
print(node7.leftChild)

print("right child of the node is:")
print(node7.rightChild)
"""