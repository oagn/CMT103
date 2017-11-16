# Node.py

class Node():
	def __init__(self, _ele=None, _next=None):
		self.element = _ele
		self.next = _next

	def __str__(self):
		return "{}-{}".format(self.element, str(self.next))