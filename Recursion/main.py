# counter = 0

# def inception():
# 	global counter
# 	if counter > 3:
# 		return 'Done'
# 	counter+=1
# 	return inception()
	

# print(inception())
"""
1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and return when needed. Usually you have 2 returns
"""

# Exercise findFactorialRecursive, findFactorialIterative

# def findFactorialRecursive(number): # O(n)
# 	answer = 1
# 	if number <= 1:
# 		return answer
# 	return number * findFactorialRecursive(number-1)

# def findFactorialIterative(number): # O(n)
# 	answer = 1
# 	while number > 1:
# 		answer = number * answer
# 		number-=1
# 	return answer

# print(findFactorialRecursive(5))
# print(findFactorialIterative(5))

# Exercise fibonacciIterativeRecursive, fibonacciIterative

def fibonacciRecursive(n):
	if n < 2:
		return n
	return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciIterative(n):
	# My solution
	# prev = 0
	# curr = 1
	# i = 0
	# while i < n:
	# 	currCopy = curr
	# 	curr = curr+prev
	# 	prev = currCopy
	# 	i+=1
	# return prev
	arr = [0, 1]
	for i in range(2, n+1):
		arr.append(arr[i-2] + arr[i-1])
	return arr[n] 

print(fibonacciIterative(3))
# print(fibonacciRecursive(8))