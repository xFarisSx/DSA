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
			holdingPointer = self.top.copy()
			self.top['next'] = holdingPointer
			self.top['value'] = value

		self.length+=1

		return self.__str__()

	def pop(self):
		if not self.top: return None
		if self.top == self.bottom:
			self.bottom = None
		holdinPointer = self.top.copy()
		self.top = holdinPointer['next']
		self.length -= 1

		return holdinPointer

	def __str__(self):
		return f'{self.top}'

myStack = Stack()
myStack.push('Google')
myStack.push('Udemy')
print(myStack.push('Discord'))
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack)
print(myStack.peek())