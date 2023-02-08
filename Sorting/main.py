import math

# letters = ['a', 'd', 'z', 'e', 'r', 'b']
# basket = [2, 65, 34, 2, 1, 7, 8]

# print(sorted(letters))
# print(sorted(basket))

"""
O(n log n) ??
Radix
Heap
Counting
<Elementary>
Bubble
Insertion
Selection
</Elementary>
<Complex, Divide and conquer> O(n log n)
Merge
Quick
</Complex>
"""

# Bubble Sort (Elementary)
# O(n^2)
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# def bubbleSort(arr):
# 	notsorted = True
# 	while notsorted:
# 		notsorted = False
# 		for i in range(0, len(arr)):
# 			if i < len(arr) - 1:
# 				if arr[i] > arr[i+1]:
# 					notsorted = True
# 					arr[i], arr[i+1] = arr[i+1], arr[i]

# 	return arr

# print(bubbleSort(numbers))

# Selection Sort
# O(n^2)
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# def selectionSort(arr):
# 	smallest = arr[0]
# 	lastI = None
# 	for j in range(0, len(arr)-1):
# 		for i in range(j, len(arr)):
# 			if arr[i] < smallest:
# 				smallest = arr[i]
# 				lastI = i

# 		temp = arr[j]
# 		arr[lastI] = temp
# 		arr[j] = smallest
# 		smallest = arr[j+1]

# 	return arr

# print(selectionSort(numbers))

# Insertion Sort
# It is used when u know if the arr already near to be sorted, it be O(1)
# O(n^2)
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# def InsertionSort(arr):
# 	# newArr = []
# 	# for i in range(0, len(arr)):
# 	# 	if newArr == []:
# 	# 		if arr[i] < arr[i+1]:
# 	# 			newArr.append(arr[i])
# 	# 			newArr.append(arr[i+1])
# 	# 		if arr[i] > arr[i+1]:
# 	# 			newArr.append(arr[i+1])
# 	# 			newArr.append(arr[i])
# 	# 	else:
# 	# 		if newArr[-1] < arr[i]:
# 	# 			newArr.append(arr[i])
# 	# 			continue
# 	# 		if newArr[0] > arr[i]:
# 	# 			newArr.insert(0, arr[i])
# 	# 			continue

# 	# 		for j in range(len(newArr)):
# 	# 			if newArr[j-1] < arr[i] < newArr[j]:
# 	# 				newArr.insert(j, arr[i])

# 	if (n := len(arr)) <= 1:
# 		return
# 	for i in range(1, n):
# 		key = arr[i]
 
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
# 		j = i-1
#         while j >=0 and key < arr[j] :
#                 arr[j+1] = arr[j]
#                 j -= 1
#         arr[j+1] = key

# 	return newArr

# print(InsertionSort(numbers))

# Merge Sort O(n log n)
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def mergeSort(arr):
	if len(arr) == 1:
		return arr

	left = arr[:math.floor(len(arr)/2)]
	right = arr[math.floor(len(arr)/2):]

	return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
	newArr = []
	leftI = 0
	rightI = 0
	while leftI < len(left) and rightI < len(right):
		if left[leftI] < right[rightI]:
			newArr.append(left[leftI])
			leftI+=1
		else:
			newArr.append(right[rightI])
			rightI+=1

	return newArr + left[leftI:] + right[rightI:]

answer = mergeSort(numbers)
print(answer)
print(numbers)