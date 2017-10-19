# no_duplicate_inplace.py
def no_duplicate_inplace(l):
	'''This function takes a list, removes duplicate values and returns the list'''
	for i in range(len(l)-1, -1, -1):
		if l[i] in l[:i]:
			del l[i]	
	return l


# Main
alist = [2, 34, 67, 1, 34, 67, 8, 9, 2, 5, 6, 7, 8, 10, 23, 34]
blist = [2,2,3,2]

print(no_duplicate_inplace(alist))