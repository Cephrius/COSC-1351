
n = int(input("Enter the number of values: "))
value = [0]* n # createing a fixed size array
# value = []

# prmopt the user to enter the number of values they will input 


for i in range(n):
    values = int(input("Enter a number: ")) # placeing an element at index i
    value[i] = values
    
print(value[::-1])

# # other way to reverse

# for i in range(n): 
#     print(value[n-i-1], end=", ")