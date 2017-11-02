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


def newRhyme(rhyme, mdict,keys):
	''' This function takes a rhyme (string with {key} placeholders) and a dictionary as input, and
	replaces {key} with the corresponding value from the dictionary. 
	After this the rhyme is saved to a file in H:\My Documents\CMT103\Lab\Wk4, read and printed.
	NB: If a file with the name dict[a]_dict[b] already exists, this will be overwritten'''
	filename = mdict[keys[0]]+"_"+mdict[keys[1]]
	with open("H:\\My Documents\\CMT103\\Lab\\Wk4\\"+filename+".txt", 'w+') as theFile:
		for i in range(len(keys)):
			rhyme = rhyme.replace('{'+keys[i]+'}',mdict[keys[i]])
		theFile.write(rhyme)
		theFile.seek(0)
		print(theFile.read())
	theFile.close()
	return 0



# Main
# The two following tuples will be taken as input by the mkDict function
def main():
	rhyme = "{a} and {b} {c} up the {d} \n to fetch a {e} of {f}"
	ids=('a','b', 'c', 'd', 'e', 'f')
	mywords=('Tim', 'Sara', 'flew', 'space', 'pair', 'slippers')

	# Print the distionary
	myDict = mkDict(ids,mywords)

	newRhyme(rhyme,myDict,ids)

if __name__ == "__main__":
	main()