class node():
    def __init__(self, data=None) -> None:
        self.data = data # <---- Where we store the past data point
        self.next = None # <---- Storing the pointer for the next data point
        
class linked_list:
    def __init__(self) -> None:
        self.head = node() #<---- Have head node available 
        
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node  = current_node.next
        current_node.next = new_node
        
    # find the length of the nodes
    def length(self):
        current = self.head
        total = 0
        while current != None:
            total += 1
            current = current.next
        return total
    
    # display contents of our list
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements) 
        
    def get(self, index):
        if index >= self.length():
            print ("ERROR: Index out of range")   
            return None
        current_index = 0
        current_node = self.head
        while True: 
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1 
            
            
    def erase(self, index):
        if index >= self.length():
            print("ERORR index out of range")
            return 
        current_index = 0
        current_node = self.head
        while True: 
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
my_list = linked_list()


my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)

my_list.display()

print("element at 2nd index:", my_list.get(2))

my_list.erase(3)
my_list.display()