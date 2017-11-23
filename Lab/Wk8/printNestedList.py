# printNestedList.py
# Week 8, task 1
def print_nested_list(nested):
	'''Input: nested list'''
	'''Output: the function prints each element in the nested list in the order they appear'''
	for i in range(len(nested)):
		# Condition for recursion, if the element is a list
		if type(nested[i]) == list:
			print_nested_list(nested[i])
		else:
			print(nested[i], end=' ')
	



def main():
	nestList =  [[2, 3, [4, 5, [6]]], [7, 8, [[9]]], [], 10, [11]]
	print_nested_list(nestList)

if __name__ == '__main__':
	main()