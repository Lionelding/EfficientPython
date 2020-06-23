# Item 32: Lazy Attributes
"""
1. Lazy access: `__getattr__()` + `setattr()`
2. `__getattribute__` is called every time if an attribute is accessed
3. `__setattr__()` saves attribute
4. Avoid the infinite loop by calling the `super().__XXX___()` from the instance setter and getter
"""

## Example 1: Usage of `__getattr__()`
'''
This feature is useful for lazy case uses. `__getattr__` only is called once the, 
and the created attributes is saved inside the instance
'''
print('################# Example 1 #################')

class LazyBD(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		value = f'Value for {name}'
		setattr(self, name, value)
		return value

class LoggingLazyBD(LazyBD):
	def __getattr__(self, name):
		print(f'Call __getattr__ {name}')
		return super().__getattr__(name)



# data = LazyBD()
# print(f'Before: {data.__dict__}')
# print(f'foo: {data.foo}')
# print(f'After: {data.__dict__}')
data2 = LoggingLazyBD()
print(f'exists: {data2.exists}')
print(f'foo: {data2.foo}')
print(f'foo: {data2.foo}')

data4 = LoggingLazyBD()
print(f'Before: {data4.__dict__}')
print(f'foo: {hasattr(data4, "food")}')
print(f'After: {data4.__dict__}')
print(f'foo: {hasattr(data4, "food")}')


# Example 2: Usage of `__getattribute__()`
"""
`__getattribute__()` is called every time when an attribute is requested, 
not matter if it exists of not.
"""
print('################# Example 2 #################')

class ValidationDB(object):
	def __init__(self):
		self.exists = 5

	def __getattribute__(self, name):
		print(f'Call __getattribute__ {name}')
		try:
			return super().__getattribute__(name)
		except AttributeError:
			value = 'Initialized'
			setattr(self, name, value)
			return value

data3 = ValidationDB()
print(f'exists: {data3.exists}')
print(f'foo: {data3.foo}')
print(f'foo: {data3.foo}')


## Example 3: Usage of `__setattr__`
"""
"""
print('################# Example 3 #################')
class SaveingDB(object):
	def __setattr__(self, name, value):
		super().__setattr__(name, value)

class LoggingSavingDB(SaveingDB):
	def __setattr__(self, name, value):
		print(f'Called __setattr__ {name} {value}')
		super().__setattr__(name, value)

data5 = LoggingSavingDB()
print(f'Before: {data5.__dict__}')
data5.foo = 50
print(f'Here: {data5.__dict__}')
data5.foo = 100
print(f'Ah: {data5.__dict__}')


## Example 4: Avoid the infinite recursion 
## by using super().__getattribute__() and super().__setattr__()
print('################# Example 4 #################')

class ValidationDB_robust(object):
	def __init__(self):
		self._data = 50

	def __getattribute__(self, name):
		# return self._data. ---> this leads to the infinite recursion 

		value = super().__getattribute__(name)
		return value


data6 = ValidationDB_robust()
print(f'_data: {data6._data}')



