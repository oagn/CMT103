# JumbleWord.py
# This program jumbles a word
import random

def jumble(the_word):
	'''Takes a string. Returns a jumbles version of that string.'''
	# Set temp word variable to the_word
	word = the_word
	# Set jumble to be an empty string
	jumble = ''

	while len(word) > 0:
		# Choose a random number within the range of the length of the current value of word
		pos = random.randint(0,len(word)-1)

		# Get the random letter from word and add it to jumble
		jumble += word[pos]

		# Remove the letter from word
		word = word[:pos] + word[pos+1:]

	return jumble

# Main

the_word = input('Enter the word or phrase you want to jumble: ')

print("\nA jumbled version of the word (phrase) '{}' is '{}'".format(the_word,jumble(the_word)))