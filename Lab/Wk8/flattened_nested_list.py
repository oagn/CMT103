# flattened_nested_list.py
# Week 8, task 2

def flatten_nested_list(nested, outList):
	'''Input: Nested list'''
	'''Output: Flattened nested list'''
	for i in range(len(nested)):
	# Condition for recursion, if the element is a list
		if type(nested[i]) == list:
			flatten_nested_list(nested[i], outList)
		else:
			outList.append(nested[i])
	return

def main():
	alist=[]
	flatten_nested_list([[2, 3, [4, 5, [6]]], [7, 8, [[9]]], [], 10, [11]], alist)
	print(alist)


if __name__ == '__main__':
	main()