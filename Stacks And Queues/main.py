# Stacks
# Google
# Udemy
# Youtube

# Arrays (Cache Locality (Better)) (Doubling up)
# Linked Lists (Extra memory, dynamic memory)

# Queues

# Matt -- Joy -- Samir -- Pavel
# Arrays
# Linked lists (there is no shifting)

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		return self.top

	def push(self, value):
		if self.bottom == None:
			self.bottom = Node(value).__dict__
			self.top = self.bottom.copy()
		else:
			pastTop = self.top.copy()
			self.top['next'] = pastTop
			self.top['value'] = value

		self.length+=1

		

	def pop(self):
		self.top = self.top['next']
		self.length -= 1

	def __str__(self):
		return f'{self.top}'

myStack = Stack()
myStack.push('Google')
myStack.push('Udemy')
myStack.push('Discord')
myStack.pop()
print(myStack.peek())