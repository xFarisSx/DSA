# Dynamic programming is a method to optimize the code
"""
By caching you don't need to repeat operations more and more
DY => Divide&Conquere + Memoization
1. Can be divided into subproblems
2. Recursive Solution
3. Are there repetitve subproblems
4. Memoize subproblems
5. Demand a raise from your boss
"""
# def memoizedAddTo80():
# 	cache = {}

# 	def func(n):
# 		if n in cache:
# 			return cache[n]
# 		else:
# 			print('Long time')
# 			cache[n] = n + 80
# 			return cache[n]

# 	return func

# memoized = memoizedAddTo80()

# print('1', memoized(5))
# print('2', memoized(5)) 
calcs = 0
def memoizedFibonacci():
	cache = {}
	global calcs
	def fibonacci(n):
		global calcs
		if n in cache:
			return cache[n]
		elif n < 2:
			return n
		else:
			print('Long time')
			cache[n] = fibonacci(n-1) + fibonacci(n-2)
			calcs+=1
			return cache[n]

	return fibonacci

memoized = memoizedFibonacci()

print('1', memoized(100))
print(calcs)
# print('2', memoized(5)) 