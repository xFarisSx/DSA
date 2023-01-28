class Stack:
	def __init__(self):
		self.array = []

	def peek(self):
		if self.array != []:
			return self.array[-1]
		else: return None

	def push(self, value):
		self.array.append(value)
		return self.array

	def pop(self):
		return self.array.pop()

	def __str__(self):
		return f'{self.array}'

myStack = Stack()
myStack.push('Google')
myStack.push('Udemy')
print(myStack.push('Discord'))
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack)
print(myStack.peek())