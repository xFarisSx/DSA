class Array:
	def __init__(self, *args):
		self.data = {

		}
		self.length = 0
		for i,el in enumerate(args):
			self.data[i] = el
			self.length+=1

	def pop(self):
		i = self.length-1
		lastItem = self.data[i]
		del self.data[i]
		self.length-=1
		return lastItem

	def push(self, item):
		self.data[self.length] = item 
		self.length+=1
		return self.length

	def shiftItems(self, i, type):
		if type == 'delete':
			for j in range(i, self.length-1):
				self.data[j] = self.data[j+1]
			del self.data[self.length-1]
			self.length-=1
		else :
			for j in range(self.length, i, -1):
				self.data[j] = self.data[j-1]
			# del self.data[self.length-1]
			self.length+=1

	def insert(self, i, el):
		self.shiftItems(i, 'insert')
		self.data[i] = el


	def delete(self, i) :
		item = self.data[i]
		self.shiftItems(i, 'delete')
		return item

	def __str__(self):
		return f'{[i for i in self.data.values()]}'
		# return f'{self.data}'

	def __getitem__(self, i):

		if i < 0:
			return self.data[self.length+i]
		return self.data[i]

	def __add__(self,new):
		self.data[self.length] = new
		self.length+=1
		return self
		
a = Array(1, 2, 3, 4, 5, 6)
# a.push(5)
# print(a.pop())
# a.delete(0)
# a.insert(3,3)

print(a)