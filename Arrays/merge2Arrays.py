def mergeSortedArrays(arr1, arr2):
	mergedArr = []
	i1 = 0
	i2 = 0
	arr1I = arr1[0]
	arr2I = arr2[0]

	while arr1I or arr2I:
		if arr1I and ( not arr2I or arr1I < arr2I):
			mergedArr.append(arr1I)
			i1 +=1
			if len(arr1) > i1:
				arr1I = arr1[i1]
			else: arr1I = None
		elif arr2I:
			mergedArr.append(arr2I)
			i2 +=1
			if len(arr2) > i2:
				arr2I = arr2[i2]
			else: arr2I = None

	return mergedArr


arr1 = [1, 5, 10]
arr2 = [2, 9 ,50]

print(mergeSortedArrays( arr1, arr2))
