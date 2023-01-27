# basket = ['apples', 'grapes', 'pears']

# # linked list: apples --> grapes --> pears
# # appels
# # 3453 --> grapes
# # 		   45354 --> pears 
# # 				     4353	--> null 

# obj1 = {
# 	'a': True
# }
# obj2 = obj1

# 1-10-99-5-16

# myLinkedList = {
# 	'head':{
# 	  'value':10,
# 	  'next':{
# 		  'value':5,
# 		  'next':{
# 			  'value':16,
# 			  'next':None
# 	  		}
# 		}
#     }
# }

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None



class LinkedList:
	def __init__(self, value):

		self.head = Node(value).__dict__

		self.tail = self.head
		self.length = 1

		self.data = { 
			'Head':self.head,
			'Tail': self.tail,
			'Length': self.length	
		}

	def append(self, value):
		newNode = Node(value).__dict__
		self.tail['next'] = newNode
		self.tail = newNode
		self.length+=1

		self.update()

		return self.printList()

	def prepend(self, value):
		newNode = Node(value).__dict__
		newNode['next'] = self.head
		self.head = newNode
		self.length+=1

		self.update()

		return self.printList()

	def printList(self):
		myArr = []
		currentNode = self.head
		while currentNode != None:
			myArr.append(currentNode['value'])
			currentNode = currentNode['next']
		return myArr

	def insert(self, i, value):
		if i >= self.length:
			self.append(value)
			self.length+=1
			self.update()
			return self.printList()

		if i == 0:
			self.prepend(value)
			self.length+=1
			self.update()
			return self.printList()

		leader = self.traverseToIndex(i)

		nextNode =  {
			'value': leader['value'],
			'next': leader['next']
		}
		
		leader['value'] = value
		
		leader['next'] = nextNode

		self.length+=1
		self.update()

		return self.printList()

	def delete(self, i):

		if i >= self.length-1:
			currentNode = self.traverseToIndex(self.length-2)
			currentNode['next'] = None

			self.length-=1
			self.update()
			return self.printList()
		if i < 0:
			self.head = self.head['next']

			self.length-=1
			self.update()
			return self.printList()

		currentNode = self.traverseToIndex(i)
		olmasiGereken = {
			'value': currentNode['next']['value'],
			'next': currentNode['next']['next']
		}
		currentNode['value'] = olmasiGereken['value']
		currentNode['next'] = olmasiGereken['next']

		self.length-=1
		self.update()

		return self.printList()

	def traverseToIndex(self, i):

		if 0 <= i <= self.length-1: 

			currentNode = self.head
			curI = 0

			while curI != i:
				currentNode = currentNode['next']
				curI+=1

			return currentNode
		else : return Node(None).__dict__

	def update(self):
		self.data = { 
			'Head':self.head,
			'Tail': self.tail,
			'Length': self.length	
		}

	def reverse(self):
		# My Way:
		myArr = self.printList()
		print(myArr)

		self.head = {
			'value':myArr[-1],
			'next':{

			}
		}

		currentNode = self.head['next']

		for index,i in enumerate(myArr[-2::-1]):
			currentNode['value'] = i
			currentNode['next'] = {

			}
			if index == len(myArr)-2:
				currentNode['next'] = None 
				self.tail = currentNode
				break
			currentNode = currentNode['next']
			
		self.update()
		#Other:
		# if(not self.head['next']):
		# 	return self.head

		# first = self.head
		# self.tail = self.head
		# second = first['next']
		# while(second):
		# 	temp = second['next']
		# 	second['next'] = first
		# 	first = second
		# 	second = temp

		# self.head['next'] = None
		# self.head = first

		# self.update()

		return self.printList()

	def __getitem__(self, i):
		currentNode = self.traverseToIndex(i)
		return currentNode['value']

	def __str__(self):
		return f'{self.printList()}'
		# return f'{self.data}'


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2, 99)
myLinkedList.insert(3, 29)
# myLinkedList.delete(2)
myLinkedList.reverse()
print(myLinkedList)
# print(myLinkedList)

# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self, value):

# 		self.head = Node(value).__dict__

# 		self.tail = self.head
# 		self.length = 1

# 		self.data = { 
# 			'Head':self.head,
# 			'Tail': self.tail,
# 			'Length': self.length	
# 		}

# 	def append(self, value):
# 		newNode = Node(value).__dict__
# 		newNode['prev'] = self.tail
# 		self.tail['next'] = newNode
# 		self.tail = newNode
# 		self.length+=1

# 		self.update()

# 		return self.printList()

# 	def prepend(self, value):
# 		newNode = Node(value).__dict__
# 		newNode['next'] = self.head
# 		self.head['prev'] = newNode
# 		self.head = newNode
# 		self.length+=1

# 		self.update()

# 		return self.printList()

# 	def printList(self):
# 		myArr = []
# 		currentNode = self.head
# 		while currentNode != None:
# 			myArr.append(currentNode['value'])
# 			currentNode = currentNode['next']
# 		return myArr

# 	def insert(self, i, value):
# 		if i >= self.length:
# 			self.append(value)
# 			self.length+=1
# 			self.update()
# 			return self.printList()

# 		if i == 0:
# 			self.prepend(value)
# 			self.length+=1
# 			self.update()
# 			return self.printList()

# 		leader = self.traverseToIndex(i-1)

# 		nextNode =  {
# 			'value': leader['next']['value'],
# 			'next': leader['next']['next'],
# 			'prev': None
# 		}
# 		nextNode['prev'] = leader
		
# 		leader['next']['value'] = value
		
# 		leader['next']['next'] = nextNode
# 		leader['next']['next']['prev'] = nextNode

# 		self.length+=1
# 		self.update()

# 		return self.printList()

# 	def delete(self, i):

# 		if i >= self.length-1:
# 			currentNode = self.traverseToIndex(self.length-2)
# 			currentNode['next'] = None

# 			self.length-=1
# 			self.update()
# 			return self.printList()
# 		if i < 0:
# 			self.head = self.head['next']
# 			self.head['prev'] = None
# 			self.length-=1
# 			self.update()
# 			return self.printList()

# 		currentNode = self.traverseToIndex(i)
# 		olmasiGereken = {
# 			'value': currentNode['next']['value'],
# 			'next': currentNode['next']['next']
# 		}
# 		currentNode['value'] = olmasiGereken['value']
# 		currentNode['next'] = olmasiGereken['next']
# 		currentNode['next']['next']['prev']

# 		self.length-=1
# 		self.update()

# 		return self.printList()

# 	def traverseToIndex(self, i):

# 		if 0 <= i <= self.length-1: 

# 			currentNode = self.head
# 			curI = 0

# 			while curI != i:
# 				currentNode = currentNode['next']
# 				curI+=1

# 			return currentNode
# 		else : return Node(None).__dict__

# 	def update(self):
# 		self.data = { 
# 			'Head':self.head,
# 			'Tail': self.tail,
# 			'Length': self.length	
# 		}

# 	def __getitem__(self, i):
# 		currentNode = self.traverseToIndex(i)
# 		return currentNode['value']

# 	def __str__(self):
# 		return f'{self.printList()}'
# 		# return f'{self.data}'

# myLinkedList = DoublyLinkedList(10)
# myLinkedList.append(5)
# myLinkedList.append(16)
# myLinkedList.prepend(1)
# myLinkedList.insert(2, 99)
# myLinkedList.insert(3, 29)
# myLinkedList.delete(2)
# print(myLinkedList)
# # print(myLinkedList)