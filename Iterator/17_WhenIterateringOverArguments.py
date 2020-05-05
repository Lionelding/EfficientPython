# Item 17: When Iterating Over Arguments
'''
iter(foo) -> foo.__iter__ -> returns an iterator object -> iterator.__next__
Advantages:
	1. Object has __iter__ which further calls an iterator further calling a `next` built-in function.
	2. To check if an object is iterator: `iter(object) is `iter(object)`
Watch-out:
	1. An iterator only produces the results once. Many standard functions expect `StopIteration` exception to be raised.
	2. A container object will read the data multiple times
'''

## inputs
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

## `Option 1`: A Standard way
def normalize(numbers):
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

print(normalize(numbers))


## `Option 2`: Use one iterator and saves the results
def normalize_copy(iterator):
	numbers = list(iterator)
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

print(normalize_copy(iterator))

## `Option 3`: iterator protocol
class ReadNumbers(object):
	def __init__(self, data):
		self.data = data
	def __iter__(self):
		return iter(self.data)

rn = ReadNumbers(numbers)
percentages = normalize(rn)
print(percentages)


def normalize_defensive(numbers):
	if iter(numbers) is iter(numbers):
		raise TypeError('Input Type is Wrong')
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

print(normalize_defensive(numbers))
print(normalize_defensive(ReadNumbers(numbers)))
# print(normalize_defensive(iter(numbers)))
