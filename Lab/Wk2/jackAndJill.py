# jackAndJill.py

# this program asks the user for two names. 
# it then prints a rhyme where place holders have been replaced for these two names
def replaceNames(rhyme, name, child):
	rhyme = rhyme.replace(name,child)

def printRhyme(rhyme, sep):
	'''Takes a rhyme with lines seperated by sep and returns the rhyme line by line'''
	rhymeLines = rhyme.replace(sep,'\n')
	return rhymeLines


# Main
rhyme = "childA and childB went up the hill, /to fetch a pail of water./childA fell down and broke his crown,/and childB came tumbling after."

child1 = input("Please enter your first child's name: ")
child2 = input("\nPlease enter your second child's name: ")

rhyme = replaceName(rhyme, 'childA',child1)
rhyme = replaceName(rhyme, 'childA',child1)

print("		{} {}	".format(child1, child2))
print(printRhyme(rhyme, '/'))