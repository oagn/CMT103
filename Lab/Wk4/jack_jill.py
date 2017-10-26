# jack_jill1.py
# This program includes a function that takes two tuples (keys and values) as input.
# It then creates and returns a dictionary.

def mkDict(keys, values):
	'''The mkDict function tables two tuples (keys and values) that need to be of the same length and returns
	a dictionary.'''
	# Check that the two tuples are of the same length
	if len(keys) != len(values):
		return 'ERROR: The two tuples are of different length'
	else:
		myDict = {}
		for i in range(len(keys)):
			myDict[keys[i]] = values[i] 
		return myDict



# Main
# The two following tuples will be taken as input by the mkDict function
def main():
	ids=('a','b', 'c', 'd', 'e', 'f')
	mywords=('Tim', 'Sara', 'flew', 'space', 'pair', 'slippers')

	# Print the distionary
	print(mkDict(ids,mywords))

if __name__ == "__main__":
	main()