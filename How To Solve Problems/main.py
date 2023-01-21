# Given 2 arrays , create a function that let's user know whether these 2 arrays contain any common items
# arr1 = ['a', 'b', 'x', 'c']
# arr2 = ['z', 'y', 'i'] False
# arr1 = ['a', 'b', 'x', 'c']
# arr2 = ['z', 'y', 'x'] True

# 2 param-arrays - no size limit; return true, false
# Easy O(a*b) O(1) Space Complexity

arr1 = ['a', 'b', 'x', 'c']
arr2 = ['z', 'y', 'x']
# def containsCommon(arr1, arr2):
# 	for i in arr1:
# 		for j in arr2:
# 			if i==j:
# 				return True
			

# 	return False
# print(containsCommon(arr1,arr2))

# HashTables = Objects in javascript
# def containsCommon(arr1, arr2):
# 	if not (isinstance(arr1, list) and isinstance(arr2, list)): return False

# 	map = {

# 	}

# 	for el in arr1:
# 		if not map.get(str(el)):
# 			map[str(el)]=True

# 	for el in arr2:
# 		if map.get(str(el)):
# 			return True

# 	return False

# print(containsCommon(arr1,arr2)) # O(a + b) Time Complexity O(a) Space Complexity

# Naive
# def hasPairWithSum(arr, sum):
# 	for i in range(len(arr)):
# 		for j in range(i+1, len(arr)):
# 			if arr[i] + arr[j] == sum:
# 				return True
# 	return False

# print(hasPairWithSum([6,4,3,2,1,7], 10))

# Better
# def hasPairWithSum2(arr, sum):
# 	mySet = set()
# 	for i in arr:
# 		if i in mySet:
# 			return True
# 		mySet.add(sum - i)
# 	return False

# print(hasPairWithSum2([6,4,3,2,1,7], 10))