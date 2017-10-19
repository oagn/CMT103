# intersect.py

# The following program produces a list composed of elements that belong to both of two given tuples.

def intersect(tA, tB):
	''' This functions take two tuples as input and return a list of elements present in both tuples'''
	# Define empty list to collect elements
	t = []

	#Loop through one tuple to compare agains elements in second tuple
	for elt in tA:
		if elt in tB:
			t.append(elt)

	return t 

# Main
tupleA = (2,3,4,6,7,8)
tupleB = (5,1,2,7,8,10,35)

print(intersect(tupleA, tupleB))

