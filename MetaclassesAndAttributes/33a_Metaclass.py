# Item 33a: Metclass
"""
1. `Type` is a metaclass, of which classes are instances.
2. Any class in Python3 (new-style) is an instance of the type metaclass
3. Use type to create a new class dynamically
4. Manually change the behavior 
5. Metaclass syntax
6. Everything is an object in Python, and they are all either 
instances of classes or instances of metaclasses.
"""

# x is an instance of Foo
# Foo is an instance of type metaclasss
# type is also an instance of type metaclasss. It instaniates itself.
class Foo():
	pass

x = Foo()
print(type(x))
print(type(Foo))

print("######### Example 1 #########")
## Example 1: type(<name>, (), {})

Foo = type('Foo', (), {})
x = Foo
print(x)

# Same as below
# class Foo:
# 	pass

print("######### Example 2 #########")
## Example 2: type(<name>, <bases>, <dict>)

Bar = type('Bar', (Foo, ), dict(attr=100))

# Same as below
# class Bar(Foo):
# 	attr = 100

y = Bar()
print(y.attr)
print(y.__class__)
print(y.__class__.__bases__)

print("######### Example 3 #########")
## Example 3: type(<name>, (), <dict>)

Foo = type('Foo', (), {'attr':100, 'attr_val':lambda x: x.attr})
foo = Foo()
print(foo.attr, foo.attr_val())

# class Foo:
#     attr = 100
#     def attr_val(self):
#         return self.attr


print("######### Example 4 #########")
## Example 4: Customized function
"""
class Foo:
	pass
foo = Foo()

Executation order:
1. Foo's parent class's __call__() is invoked.  --- > type's __call__() is invoked
2. __call__() invokes __new__()
3. __call__() invokes __init__()
"""

def new(cls):
	x = object.__new__(cls)
	x.attr = 100
	return x

Foo.__new__ = new
f = Foo()
g = Foo()
print(f.attr, g.attr)


print("######### Example 5 #########")
## Example 5: Generalizion via using Metaclass
## Python forbids the change of behavior of `type`, but we can inherent a new one from `type`
class Meta(type):
	def __new__(cls, name, bases, dct):
		print(cls, name, bases)
		x = super().__new__(cls, name, bases, dct)
		x.attr = 100
		return x
"""
1. Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class
2, Assigns the custom attribute attr to the class, with a value of 100
3. Returns the newly created class
"""

class Foo(metaclass=Meta):
	print('1')
	pass
	print('2')

## Class Factory
class Meta2(type):
	def __init__(cls, name, bases, dct):
		cls.attr = 123

class X(metaclass=Meta2):
	pass

class Y(metaclass=Meta2):
	pass

class Z(metaclass=Meta2):
	pass

print(X.attr, Y.attr, Z.attr)





# REF: https://realpython.com/python-metaclasses/

