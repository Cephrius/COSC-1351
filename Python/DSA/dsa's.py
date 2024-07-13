# INDEXING

# string 
from DataStructuresAndAlgorithimsInPython.linkedList import Node


x = 'frog'
print(x[3])

# list
y = ['pig', 'cow', 'horse']
print(y[2])

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z[0])


# SLICING - slice out substrings, sublists, subtuples using indexes.
# [start: end+1 : step]
# if you dont delcare a start the start defaults the beginning same with end and step...

x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:]) #<--- starts from the last three char...
print(x[:-2]) #<----- Starts from right side 


#Adding and concatinating
# combining 2 sequences of the same type by using + 

# string
x = 'horse' + 'shoe'
print(x)

# list 
y = ['pig', 'cow'] + ['horse']
print(y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny') + ('Craig',)
print(z)


#multiplying - multiply a sequence using *

# string 
x = 'bug' * 3
print(x)

# list
y = [8, 5] * 3
print(y)

# tuple
z = (2, 4) * 3
print(z)


# checking membership - test whether an item is or is not in a sequence

# string
x = 'bug'
print('u' in x)

#list 
y = ['pig', 'cow', 'horse']
print('cow' not in y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print('Niklas' in z)


# iterating - iterating throught the items in a sequence

# item
x = [7, 8, 3]
for item in x:
    print(item)
    
# index & item
y = [7, 8, 3]
for index, item in enumerate(y):
    print(index, item)


# number of items - count the number of items in a sequence

# string
x = 'bug'
print(len(x))

# list
y = ['pig', 'cow', 'horse']
print(len(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(len(z))


#minimum - find the minimun item in a sequence lexicographically Alpha or numberic types, but cannot mix types

# string
x = 'bug'
print(min(x))

y = ['pig','cow','horse']
print(min(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(min(z))


#maximum - find the maximum item in a sequence lexicorgraphically alpha or numberic types but cannont mix types

# string
x = 'bug'
print(max(x))

# list
y = ['pig', 'cow', 'horse']
print(max(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(max(z))


# sum - find the sum of items in a sequence (only works with numeric types)
# string -> error
# x = [5,7,'bug']
# print(sum(x)) # Generates an error

# list
y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))

# tuple
z = (50, 4, 7, 19)
print(sum(z))


# sorting - returns a new LIST of items in sorted order doesnt change the org list

# string
x = 'bug'
print(sorted(x)) # <--- Pulls letter out of string and returns a new list with the sorted chars..

# list
y = ['pig', 'cow', 'horse']
print(sorted(y))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z))

# sorting - sort by second letter
# Add a key parameter and a lambda function to reutrn the second character. 
# (the word key here is a defined parameter name, k is an arbritrary varible name)

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z, key=lambda k: k[1]))  # <--- sorts the tuple by the second letter in the strings


# count(item) - returns count of an item

# string
x = 'hippo'
print(x.count('p'))

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.count('Niklas'))


#index(item) - returns the index of the first occurnece of an item

# string
x = 'hippo'
print(x.index('p')) 

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.index('Niklas'))


# unpacking - unpacks the n items of a sequence into n variables

# string
x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)
print(b,c,a)



### LISTS

# -General Purpose
# - Most widely used data structure
# - grow and shrink size as needed
# - sequence type
# - sortable

# constructors - creating a new list

x = list()
y = ['a',25,'dog',8.43]
tuple1 = (10,20)
z = list(tuple1)

#list comrehenstion
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i > 4]

# delete
x = [5,3,8,6]
del(x[1])
print(x)
del(x) # list no longer exists

#append
x = [5,3,8,6]
x.append(7)
print(x)


#extend - append a sequence to a list
x = [5,3,8,6]
y = [12,13]
x.extend(y) 
print(x) 

#insert - insert an item at a given index
x = [5,3,8,6]
x.insert(1,7)
print(x)
x.insert(1, ['a', 'm'])
print(x)

