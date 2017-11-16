
class Node():
	def __init__(self, _ele=None, _next=None):
		self.element = _ele
		self.next = _next

	def __str__(self):
		return "{}-{}".format(self.element, str(self.next))

class SLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		return "LL: {}".format(str(self.head))

	def addFirst(self, _ele):
		node = Node(_ele, self.head)
		self.head = node
		if self.size == 0:
			self.tail = node
		self.size += 1

	def addLast(self, _ele):
		node = Node(_ele, None)
		if self.size > 0:
			self.tail.next = node
			self.tail = node
		else:
			self.head = self.tail = node
		self.size += 1

	def add(self, p, _ele):
		if p >= self.size:
			self.addLast(_ele)
		elif p == 0:
			self.addFirst(_ele)
		else:
			node = Node(_ele, None)
			# Locate node with index p-1
			i = 0
			currentN = self.head
			while i < p-1:
				currentN = currentN.next
				i += 1
			node.next = currentN.next
			currentN.next = node
			self.size += 1

	def removeFirst(self):
		if self.size == 0:
			return None
		else:
			ret = self.head
			self.head = self.head.next
			if self.size == 1: 
				self.tail = None
			self.size -= 1
			return ret

	def remove(self, p):
		if self.size == 0 or p >= self.size:
			return None
		elif p == 0:
			return self.removeFirst()
		else:
			i = 0
			currentN = self.head
			while 1 <= p-1:
				currentN = currentN.next
				i += 1
			ret = currentN.next
			if self.tail == currentN.next:
				self.tail = currentN
			currentN.next = currentN.next.next
			self.size -= 1
			return ret

	def removeLast(self):
		return remove(self,self.size-1)

	def getNode(self, ind):
		if ind > self.size or self.size == 0:
			return None
		else:
			i = 0
			currentN = self.head
			while i < ind:
				currentN = currentN.next
				i += 1
			return currentN

def add_List_to_LL(listType, alist):
	if listType == SLinkedList:
		ret = SLinkedList()
		for _ele in alist:
			ret.addFirst(_ele)
		return ret
#	elif listType == 'DLinkedList':
#		ret = DLinkedList()
#		for _ele in alist:
#			ret.addFirst(_ele)
#		return ret
	else: print("Please specify SLinkedList or DLikedList")


def main():

	alist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	sll = add_List_to_LL(SLinkedList, alist)
	print(sll)

	print("The element of Node at position {} is {}".format(3, sll.getNode(3).element))



if __name__ == '__main__':
	main()

