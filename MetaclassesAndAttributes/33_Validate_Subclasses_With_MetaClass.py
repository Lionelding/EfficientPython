# Item 33: Validate Subclasses with Metaclasses
"""
1. Use metaclass to ensure/validate the subclass are well formed at the time they are defined
2. The `__new__()` method of metaclass is run after the class statement's entire body is accessed.
"""

# Example 1: Simple Metaclass
print("######### Example 1 #########")
class Meta(type):
	def __new__(meta, name, bases, class_dict):
		print(meta, name, bases, class_dict)
		return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
	stuff = 123
	def foo(self):
		pass

# Example 2:
print("######### Example 2 #########")
class ValidatePolygon(type):
	def __new__(meta, name, bases, class_dict):
		print(f'meta: {meta}')
		print(f'name: {name}')
		print(f'bases: {bases}')
		print(f'class_dict: {class_dict}')
		if bases != (object,):
			if class_dict['sides'] < 3:
				raise ValueError(f'Polygons need 3+ class_dict')
		return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
	sides = None
	print('1')

	@classmethod
	def interior_angles(cls):
		return (cls.sides - 2) * 180

	print('2')

class Triangle(Polygon):
	print('3')
	sides = 3
	print('4')


# print(f'Before Class')
# class Line(Polygon):
# 	print('Start')
# 	sides = 1
# 	print('Finish')
# print(f'After class')

