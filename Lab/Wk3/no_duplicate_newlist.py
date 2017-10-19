# no_duplicate_newlist.py

def no_duplicate_newlist(l):
	''' This function creates a new list from the input list, taking away all duplicate values'''
	lNew = []
	for val in l:
		if val not in lNew:
			lNew.append(val)
	return lNew

# Main
alist = [2, 34, 67, 1, 34, 67, 8, 9, 2, 5, 6, 7, 8, 10, 23, 34]

print(no_duplicate_newlist(alist))