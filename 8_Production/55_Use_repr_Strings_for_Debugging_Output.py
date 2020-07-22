# Item 55: Use repr Strings for Debugging Output
"""
1. Calling `print` on built-in types will show the human-readable info, but also hides the value type
2. Calling `repr` on built-in types will produce the printable strings version of a value, 
which further to get the originial value by calling the `eval` function. 
3. Define `__repr__` to customize printable representation of a class
4. Acessing `instance.__dict__` as an alternative way.
"""


print('######### Example 1 #########')
## Example 1: Python built-in object


num_str = '5'
num_int = 5
print(num_str)
print(num_int)

print(f'repr: {repr(num_str)}')
print(f'eval(repr): {eval(repr(num_str))}')
print(num_int)

print(f'f-string: {num_str}')
print(f'f-string: {num_int}')


print('######### Example 2 #########')
## Example 2: Dynamic Python Object

class MyClass:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Instance Attributes are {self.x}, {self.y}'
myclass1 = MyClass(10, 100)
print(myclass1)

print(f'Attributes Dict: {myclass1.__dict__}')