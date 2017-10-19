# flipcoin.py

# This program flips a coin a user specified number of times and then tells you the number of heads and tails

import random

def flip():
	'''Returns 0 (heads) or 1 (tails)'''
	return random.randint(0,1)

# Main
# ask the user for the desired number of coin flips
coinFlips = int(input("How many times do you want to flip the coin? Be reasonable and keep it between 0 and 10,000: "))

# check that the user stays within the given constraints
# if they don't, ask again
while coinFlips not in range(0,10001):
	print("Come on...")
	coinFlips = int(input("\nHow many times do you want to flip the coin? Be reasonable and keep it between 0 and 10,000: "))

coin = 2

heads = tails = 0

for coins in range(coinFlips):
	# flip the coin
	coin=flip()

	# check whether you got heads or tails and add to counters
	if coin == 0:
		heads += 1
	else: 
		tails += 1

print("Heads: {} \nTails: {}".format(heads, tails))