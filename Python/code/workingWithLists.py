

# BINARY SEARCH

numbers = [1,10,30,50,65,90,105,200]
n = len(numbers)
found = False
first = 0
last = n -1 
mid = 0

## Get user input for the number he/she is looking for
num = int(input("Enter the number you are looking for: "))

while(first <= last and found != True):
    mid = (first + last) // 2 # Calculate the index of the middle element
    if(numbers[mid] == num):
        found = True
    elif (numbers[mid] > num):
        last = mid-1
    else:
        first = mid + 1
if(found == False):
    print("Not Found")
else:
    print(found)
    print(mid)





#SELECTION

'''
numbers = [8,5,7,1,9,3,6,2]
n = len(numbers) # this is storing the size of our list

for i in range(0, n-1):
    minPosition = i

    for j in range(i + 1, n):                   # this is the loop that will find the 
      if(numbers[j] < numbers[minPosition]):    #   position of the smallest element
            minPosition = j
    
    #swap the elements at positions i and j in the list
    temp = numbers[i]
    numbers[i] = numbers[minPosition]
    numbers[minPosition] = temp

print(numbers)
'''






"""

# Swapping varibles


list_a = [0,2,31,4,5,7]


index1 = list_a.index(0)
index2 = list_a.index(2)

list_a[index1],list_a[index2] = list_a[index2],list_a[index1]

print(list_a)                       


"""