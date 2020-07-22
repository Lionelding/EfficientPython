# Item 42: Decorator with functools_wraps
"""
1. Decorators allow one func to modify any other func at the runtime
2. Decorators come with side-effect
3. functools.wrap wraps the decorator to avoid this issue
"""

from functools import wraps

def trace(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		print(f'result: {result}, func name: {func.__name__}, input: {args}, {kwargs}')
		return result
	return wrapper


@trace
def fibonacci(n):
	"""
	Compute n-th fibonacci number
	"""
	if n in (0, 1):
		return n
	return (fibonacci(n - 2) + fibonacci(n - 1))

fibonacci(3)

help(fibonacci)