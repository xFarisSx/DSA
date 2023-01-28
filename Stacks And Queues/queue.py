
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first

	def enqueue(self, value):
		if not self.last:
			self.last = Node(value).__dict__
			self.first = self.last
		else:
			self.last['next'] = Node(value).__dict__
			self.last = self.last['next']

	def dequeue(self):
		if not self.first:
			return None
		if self.first == self.last:
			self.last = None
		holdinPointer = self.first
		self.first = self.first['next']
		return holdinPointer

	def __str__(self):
		return f'{self.first}'

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.peek())

