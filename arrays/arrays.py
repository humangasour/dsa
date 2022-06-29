strings = ['a', 'b', 'c', 'd']
# 4 * 4 - takes 16 bytes in memory (in a 32-bit system)

# lookup
print(strings[1])  # O(1)
# the computer knows the address of the index in memory

# push
strings.append('x')  # O(1)
"""
there might be times when computer does not have enough memory to append an item to the array
at it's current location. So it will need to shift the entire array to another location, and in that case
the complexity of append or push would be O(n)
"""

# pop
strings.pop()  # O(1)
strings.pop(0)  # O(n)

# insert at the beginning
strings.insert(0, 'x')  # O(n)
# the index of all the other elements has to shift to make space for the new element

strings.insert(2, 'alien')  # O(n)

# Array native python methods :-
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# ort()	Sorts the list

# List objects are implemented as arrays.
# They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v)
# operations which change both the size and position of the underlying data representation.

# For in depth information on arrays
# https://docs.python.org/3/tutorial/datastructures.html

# to implement arrays as a stack
# https://docs.python.org/3/library/collections.html#collections.deque
