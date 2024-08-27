number = int(input("Enter a size: "))

for i in range(number): # <--- itterate based on size
    for j in range(i+1): # <--- How many times in each line
        print(i+1, end=" ")
    print()
    
    # print(str(i+1)*(i+1) )  alternative method