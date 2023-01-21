def reverse(string):
	if not isinstance(string, str) or len(string) < 2:
		return

	arr = []
	for i in range(len(string)-1, -1, -1):
		arr.append(string[i])


	return ''.join(arr)

	# return string[len(string):0:-1]+ string[0]

# print(reverse('faris')) #siraf
# print(reverse('omar'))
