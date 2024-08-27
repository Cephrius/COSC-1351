# a list containing the frequencies of the 11 possible sums (2 through 12)
# this initializes a list of 11 elements, all with the value 0
dice_sums = [0] * 11

# display the possible rolls of two dice
print ("Die1\tDie2\tSum")
# iterate through the values of die 1
for die1 in range(1, 7):
	# for each value of die 1, iterate through the values of die 2
	for die2 in range(1, 7):
		# calculate the sum of both dice
		dice_sum = die1 + die2
		# increment the frequency of each sum
		# the smallest possible sum, 2, is at index 0 of the list
		# so subtract 2 from the index
		# the frequency of rolling a 2 is at index 0 of the list
		dice_sums[dice_sum - 2] += 1

		# display the values for this roll
		print ("{}\t{}\t{}".format(die1, die2, dice_sum))

# display the sum frequencies
print ("\nSum\tFreq\tProb")
for i in range(len(dice_sums)):
	# i starts at 0, but we want to begin the sums at 2
	print ("{}\t{}\t{}".format(i + 2, dice_sums[i], dice_sums[i] * 1.0 / sum(dice_sums)))
