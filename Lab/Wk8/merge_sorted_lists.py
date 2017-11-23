# merge_sorted_lists.py
# Week 8, task 3

def merge_sorted_lists(listA, listB):
	'''Input: two sorted lists, listA and listB, both sorted in ascending order (smallest to largest)'''
	'''Output: one sortde list, listA, with the elements from listB merged in'''

	for i in range(len(listB)):
		inserted = False
		for j in range(len(listA)):
			if listB[i] < listA[j]:
				listA.insert(j,listB[i])
				inserted = True
				break
		if inserted == False:
			listA.append(listB[i])
	return

def main():
	listA = [2, 5, 8, 10, 11]
	listB = [1, 3, 4, 6, 7, 8, 9, 11, 12, 13]
	merge_sorted_lists(listA, listB)
	print('The final listA:', listA)

if __name__ == '__main__':
	main()