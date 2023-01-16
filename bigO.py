from datetime import datetime
import numpy

# nemo = ['nemo']
# everyone = [
# 	'dory', 'bruce', 'marlin', 'nemo', 'grill', 'bloat', 'nigel', 'squirt',
# 	'darla', 'hank'
# ]
# large = ['nemo' for i in range(100)]

# def findNemo(array):
# 	t0 = datetime.now()
# 	for i in range(0,len(array)):
# 		if array[i] == 'nemo':
# 			print('Found Nemo!')
# 			break
# 	t1 = datetime.now()
# 	print('Call to find Nemo took', (t1-t0).microseconds, 'ms')
	
# findNemo(large) # O(n) --> Linear Time

# boxes = [i for i in range(6)]
# def logFirstTwoBoxes(boxes):
# 	print(boxes[0]) # O(1)
# 	print(boxes[1]) # O(1)

# logFirstTwoBoxes(boxes) # O(2)

# Challenge 1
# def funChallenge(input):
# 	a = 10 # O(1)
# 	a = 50 + 3 # O(1)

# 	for i in range(0, len(input)):
# 		anotherFunction() # O(n)
# 		stranger = true # O(n)
# 		a+=1 # O(n)

# 	return a # O(1)
# BIG O(3 + 3n) simplified to => O(n)

# Challenge 2
# def anotherFunChallenge(input):
#   a = 5 #O(1)
#   b = 10#O(1)
#   c = 50#O(1)
#   for i in range(input):
#     x = i + 1#O(n)
#     y = i + 2#O(n)
#     z = i + 3#O(n)

  
#   for j in range(input):
#     p = j * 2#O(n)
#     q = j * 2#O(n)
  
#   whoAmI = "I don't know"#O(1)
# BIG O: O(4 + 5n) => O(n)

# Rule 2:
# def printingItems(items):
# 	print(items[0])

# 	middleIndex = round(len(items)/2)
# 	index = 0

# 	while index < middleIndex:
# 		print(items[index])
# 		index+=1

# 	for i in range(100):
# 		print('hi')

# O(1 + n/2 + 100 ) => O(n)

# Rule 3:
# def compressBoxesTwice(boxes, boxes2):
# 	for box in boxes:
# 		print(box)

# 	for box2 in boxes2:
# 		print(box2)

# O(b1 + b2)

# boxes = [1, 2, 3, 4, 5]
# def logAllPairsOfArray(array):
# 	for i in array:
# 		for j in array:
# 			print(f'({i}, {j})')
# logAllPairsOfArray(boxes)
# # O(n^2)

# def compressBoxesTwice(boxes, boxes2):
# 	for box in boxes:
# 		print(box)
# 		for box2 in boxes2:
# 			print(box2)

# O(b1 * b2)

# Rule 4:
# def printAllNumbersThenAllPairSums(numbers):
# 	for number in numbers:
# 		print(number)

# 	for firstNumber in numbers:
# 		for secondNumber in numbers:
# 			print(firstNumber+secondNumber)

# printAllNumbersThenAllPairSums([1,2,3,4,5])
# O(n + n^2) => O(n^2)

# Space Complexity:
# def boo(n):
# 	for i in range(len(n)):
# 		print('boo')

# boo([1,2,3,4,5])
# # O(1)


# def arrayOfHiNTimes(n):
# 	hiArray = []
# 	for i in range(n):
# 		hiArray.append('hi')
# 	return hiArray

# arrayOfHiNTimes(5)
# # O(n)

# Find 1st, Find Nth...
# array = [{'tweet':'hi', 'date':200}, {'tweet':'my','date':2000}, {'tweet':'teddy', 'date':3030}]
# array[0]#O(1)
# array[-1] #O(1)


