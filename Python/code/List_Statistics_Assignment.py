###########################################################################################
# Name: Chiedozie Ehileme
# Date: October 12, 2022
# Description: Python program that generates a list of integers, 
#such that both its length and the integers added to the list are provided by the user
###########################################################################################

import statistics


def fillList():
	nums = []
	# (1) prompt the user for a list size
	size = int(input("How big do you want your list to be?: "))

	# (2) prompt the user for the integers to store in the list (corresponding to the list size)
	for i in range(size):
		size = int(input("Enter an integer: "))

	# (3) create the list
		nums.append(size)

	# (4) return the list
	return nums
	

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

 #print(list, end= " ")

# create the list
nums = fillList()
# display information about the list as shown in the assignment description
# (1) print the list
print("The original list: {}".format(nums))

# (2) print the length of the list
print("The length of the list is: " , (len(nums)))

# (3) find out and print the even numbers in the list
evennumbers = []
for num in range (len(nums)):
	if nums[num] % 2 == 0:
		evennumbers.append(nums[num])
		
print("The even numbers in the array are: {}".format(evennumbers))
		
# (4) compute the average of the elements and print the average
average = sum(nums) / len(nums)
print("The average of the elements in the list are: {} ".format(average))

# (5) print the reversed list
nums.reverse()
print("The reversed list: {} ".format(nums))

# (6) print the sorted list
nums.reverse()
nums.sort()
print("The sorted list: {} ".format(nums))

# (7) print the largest element in the list
print("The largest number in the list is: {}".format(max(nums)))

# (8) print the smallest element in the list
print("The smallest element in the list is: {}".format(min(nums)))

# (9) find and print the median of the list
middle = statistics.median(nums) 
print("The median of the list is: {}".format(middle))

