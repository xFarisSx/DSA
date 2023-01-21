strings = ['a', 'b', 'c' , 'd']
# 4*4 = 16 bytes

strings[2] # Lookup (constant)

#append
strings.append('e') # Push (constant)


# pop
strings.pop(-1) #O(1)
strings.pop(2) #O(n)

# insert
strings.insert(0, 'x') # O(n)
strings.insert(2, 'alien') # O(n)


print(strings)