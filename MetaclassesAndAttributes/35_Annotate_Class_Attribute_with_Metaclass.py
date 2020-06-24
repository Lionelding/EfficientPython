# Item 35: Annotate Class Attribute with Metaclass
"""
1. Metaclass is able to modify a class's attribute before the class is defined
2. Descriptors and Metaclass are powerfull combination for declarative behavior and runtime inspection
3. Avoid memory using the Descriptors and Metaclass
"""

## Example 1:
print("######### Example 1 #########")

class Field(object):
	def __init__(self, name):
		self.name = name
		self.internal_name = "_" + self.name

	def __get__(self, instance, type):
		if isinstance is None:
			return self
		return getattr(instance, self.internal_name, "Not defined")

	def __set__(self, instance, value):
		setattr(instance, self.internal_name, value)

class Customer(object):
	first_name = Field('first_name')
	last_name = Field('last_name')
	prefix = Field('prefix')
	suffix = Field('suffix')

foo = Customer()
print(f'Before: {foo.first_name}, {foo.__dict__}')
print(f'Before: {repr(foo.first_name)}, {foo.__dict__}')
foo.first_name = 'JACK'
print(f'After: {repr(foo.first_name)}, {foo.__dict__}')

## Example 2: Metaclass
print("######### Example 2 #########")

class NewField(object):
	def __init__(self):
		self.name = None
		self.internal_name = None

	def __get__(self, instance, type):
		if isinstance is None:
			return self
		return getattr(instance, self.internal_name, "Not defined")

	def __set__(self, instance, value):
		setattr(instance, self.internal_name, value)

class Meta(type):
	def __new__(meta, name, bases, class_dict):
		for key, value in class_dict.items():
			print(key, value)
			if isinstance(value, NewField):
				value.name = key
				value.internal_name = "_" + key
		cls = type.__new__(meta, name, bases, class_dict)
		return cls

class DataBaseRow(object, metaclass=Meta):
	pass


class BetterCustomer(DataBaseRow):
	print('3')
	first_name = NewField()
	last_name = NewField()
	prefix = NewField()
	suffix = NewField()
	print('4')


foo2 = BetterCustomer()
print(f'Before: {repr(foo2.first_name)}, {foo2.__dict__}')
foo2.first_name = 'JACK'
print(f'After: {repr(foo2.first_name)}, {foo2.__dict__}')