# user  = {
# 	'age':54,
# 	'name':'Kylie',
# 	'magic':True,
# 	'scream': lambda : print('aaa'),
# 	True:1,
# 	1: 45
# }

# user['age'] # O(1)
# user['spell'] = 'abra kadabra' # O(1)
# user['scream']() # O(1)
# # del user['spell'] # O(1)

# print(user[True])

# b = {1, 2}

# Implement Hash Table

class HashTable:
	def __init__(self, size , **kargs):
		self.data = [[]] * size
		for arg in kargs.items():
			self.set(arg[0], arg[1])
		
	def _hash(self, key):
		hash = 0
		for i in range(0, len(key)):
			hash = (hash + ord(key[i]) * i) % len(self.data)

		return hash

	def set(self, key, value):
		address = self._hash(key)
		if(not self.data[address]):
			self.data[address] = []
		self.data[address].append([key, value])
		
		return self.data

	def get(self, key):

		currentBucket = self.data[self._hash(key)]
		for el in currentBucket:
			if el[0] == key:
				return el[1] # O(1|n)

	def keys(self):
		keysAr = []
		for key in map(lambda y: y[0][0],filter(lambda x: x != [], self.data)):
			keysAr.append(key)

		return keysAr

myHashTable = HashTable(10, grapes = 10000, fruits = 20000)
print(myHashTable.get('grapes'))
print(myHashTable.data)
print(myHashTable.keys())

# Google Question
# def findFirstRepeat(arr):
# 	map = {

# 	}

# 	for el in arr:
# 		if map.get(el) != None :
# 			map[el]+=1
# 			return el
# 		else:
# 			map[el] = 1

# 	# return map

# print(findFirstRepeat([2,5,1,2,3,5,1,2,4]))
# print(findFirstRepeat([2,1,1,2,3,5,1,2,4]))
# print(findFirstRepeat([2,3,4,5]))

