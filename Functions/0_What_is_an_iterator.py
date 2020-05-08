# item 0: What is an iterator
'''
1. `iterator protocol`: two special functions `__iter__()` and `__next__()`.
2. An object is called iterable if we can get an iterator from it.
3. iter() --> __iter__()
'''

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(dir(my_iter))
print(next(my_iter))
print(next(my_iter))

## How the for loop works
iterable = my_list
iterator = iter(iterable)
while True:
	try:
		item = next(iterator)
		print(item)
	except StopIteration:
		break

## Build a costomized iterator
'''
`__iter__()` returns an iterator with some possible initialization 
`__next__()` returns the next item
'''
class PowTwo:
	def __init__(self, max=0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.max:
			result = self.n ** 2
			self.n = self.n + 1
			return result
		else:
			raise StopIteration
	def next(self):
		return self.__next__()

### Manually 
pt = PowTwo(5)
pt_iterator = iter(pt)
print(pt_iterator.__next__())
print(pt_iterator.__next__())
print(pt_iterator.__next__())
print(pt_iterator.__next__())
print(pt_iterator.__next__())

### For loop
for i in PowTwo(5):
	print(i)

### Infinite iterator
print(int())
z_iterator = iter(int(), 1)
