# Item 31: Descriptor
"""
1. What is a Descriptor
2. What is Descriptor Protocol
3. How to create a Descriptor
4. Types of Descriptors
5. Descriptor Syntax 
6. Examples
7. When and Why to use Descriptor
"""

## What is a Descriptor
"""
Python descriptors are created to manage the attributes of different classes which use the object as reference. 
In descriptors we used three different methods that are __getters__(), __setters__(), and __delete__(). 
If any of those methods are defined for an object, it can be termed as a descriptor.
"""

## What is Descriptor Protocol
"""
Python descriptor protocol is simply a way to specify what happens when an attribute is referenced on a model. 
It allows a programmer to easily and efficiently manage attribute access: `set`, `get`, and `delete`.

Python doesn’t have a private variables concept, 
and descriptor protocol can be considered as a Pythonic way to achieve something similar.
"""

## How to create a Descriptor
"""
You can create a descriptor a number of ways:

* Create a class and override any of the descriptor methods: __set__, __ get__, and __delete__. 
This method is used when the same descriptor is needed across many different classes and attributes, for example, for type validation.
* Use a property type to create a descriptor.
* Use @property decorators which are a combination of property type method and Python decorators.
"""

## Types of Descriptors
"""
1. if implement __get__(), then it is a `non-data descriptor`
2. if implement __set__(), __delete()__, then it is a `data descriptor`
"""

## Descriptor Syntax 
"""
* __get__(self, obj, type=None) -> object
* __set__(self, obj, value) -> None

self: the instance of the Descriptor
obj: the instance of the object that the Descriptor is attached to
type: the type of object that the Descriptor is attached to

In .__set__(), you don’t have the type variable, because you can only call .__set__() on the object. 
In .__get__() on both the object and the class.
"""


## Example 1: Creating a descriptor with a classs method
class Gear(object):
	def __init__(self, name='Empty'):
		self.name = name

	def __get__(self, obj, type):
		return f'Gear: {self.name}'

	def __set__(self, obj, name):
		self.name = name

class Car1(object):
	gear = Gear()

print('Example 1')
car1 = Car1()
print(car1.gear)
car1.gear = '1'
print(car1.gear)

## Example 2: Creating a descriptor with property type
class Car2(object):
	def __init__(self, name='Empty'):
		self._gear = name

	def fget(self):
		return f'Gear: {self._gear}'

	def fset(self, name):
		self._gear = name

	def fdel(self):
		del self._gear

	gear = property(fget, fset, fdel, 'Hellow')

print('Example 2')
car2 = Car2()
print(car2.gear)
car2.gear = '2'
print(car2.gear)

## Example 3: Creating a descriptor with @property
class Car3(object):
	def __init__(self, name='Empty'):
		self._gear = name

	@property
	def gear(self):
		return self._gear

	@gear.getter 
	def gear(self):
		return f'Gear: {self._gear}'

	@gear.setter 
	def gear(self, name):
		self._gear = name

print('Example 3')
car3 = Car3()
print(car3.gear)
car3.gear = '3'
print(car3.gear)

## Example 4: Creating a descriptor with property type at runtime
## https://developer.ibm.com/technologies/python/tutorials/os-pythondescriptors/

## Example 5: Descriptors are instantiated just once per class.
"""
because each instance of Foo shares the same descriptor instance
"""
print('Example 5')
car_a = Car1()
car_a.gear = 'car_a_gear'
car_b = Car1()
car_b.gear = 'car_b_gear'
print(f'{car_a.gear}, {car_b.gear}')

## Example 6: However, attributes created with @property or property() is instance specific
print('Example 6')
car_a = Car3()
car_a.gear = 'car_a_gear'
car_b = Car3()
car_b.gear = 'car_b_gear'
print(f'{car_a.gear}, {car_b.gear}')

## Example 7:
## With WeakKeyDictionary, Not everything can be weakly referenced. Skipped.


## Example 8: The best solution to solve the fact that Descriptor is only instantiated once. 
class AdvancedGear(object):
	def __init__(self, name='default_gear'):
		self.name = name

	# def __set_name__(self, owner, name='default_gear'):
	# 	print(owner)
	# 	self.name = name

	def __get__(self, obj, type=None):
		return obj.__dict__.get(self.name) or '0'

	def __set__(self, obj, value):
		obj.__dict__[self.name] = value

class AdvancedCar(object):
	gear = AdvancedGear('default_gear')

print('Example 8')
advanced_car_1 = AdvancedCar()
advanced_car_2 = AdvancedCar()
print(advanced_car_1.gear)
advanced_car_1.gear = '8'
advanced_car_2.gear = '9'
print(advanced_car_1.gear, advanced_car_2.gear)

## Why and When to use Descriptor
## Example 9: Use wrapper and Descriptor to store attribute values for instances after they are assigned
"""
1. Because we only implement the `__get__()`, we created a non-data descriptor.
2. For the first time that `meaning_of_life` is called, `.__get__()` is automatically called and 
executes .meaning_of_life() on the my_deep_thought_instance object.
3. The result is stored in the __dict__ attribute of the object itself. Next it is called, Python will use the lookup chain to
find a value for that attribute inside the __dict__ attribute.
"""
print('Example 9')

import time 

class MyWrapper(object):
	def __init__(self, function):
		self.function = function
		self.name = function.__name__

	def __get__(self, obj, type=None):
		obj.__dict__[self.name] = self.function(obj)
		return obj.__dict__[self.name]

class DeepThought(object):
	@MyWrapper
	def meaning_of_life(self):
		time.sleep(3)
		return 42

mythought = DeepThought()
print(mythought.meaning_of_life)
print(mythought.meaning_of_life)
print(mythought.meaning_of_life)

## Example 10: Multiple Property
"""
"""
print("Example 10")
class CheapPiece(object):
	def __init__(self, name):
		self.name = name

	def __get__(self, obj, type=None):
		return obj.__dict__.get(self.name or None)

	def __set__(self, obj, value):
		print(value>=1000)
		if value >= 1000:
			raise ValueError(f'Too Expensive')
		obj.__dict__[self.name] = value

class CarWithMultipleComponents(object):
	engine = CheapPiece('engine')
	tire = CheapPiece('tire')
	seat = CheapPiece('seat')

car10 = CarWithMultipleComponents()
print(car10.engine, car10.tire, car10.seat)
car10.engine = 10
car10.tire = 1
car10.seat = 2
print(car10.engine, car10.tire, car10.seat)


## Reference: https://realpython.com/python-descriptors/#what-are-python-descriptorss



