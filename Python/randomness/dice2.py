from random import randint, seed

# simulates the roll of a die
def roll():
	return randint(1, 6)

# get the number of rolls and seed desired
num_rolls = int(input("How many rolls of two dice would you like to simulate? "))
rand_seed = input("What pseudo-random number generator seed would you like to use? ")
dice_sums = [0] * 11

print ("Rolling two dice {} times with a seed of {}.".format(num_rolls, rand_seed))

# seed the number generator
seed(rand_seed)
print ("Die 1\tDie 2\tSum")
# roll the dice
for i in range(0, num_rolls):
	die1 = roll()
	die2 = roll()
	# calculate the sum
	dice_sum = die1 + die2
	# update the sum frequencies
	dice_sums[dice_sum - 2] += 1

	print ("{}\t{}\t{}".format(die1, die2, dice_sum))

# display a summary
print ("\nSum\tFreq\tProb")
for i in range(len(dice_sums)):
	print ("{}\t{}\t{}".format(i + 2, dice_sums[i], dice_sums[i] * 1.0 / sum(dice_sums)))

