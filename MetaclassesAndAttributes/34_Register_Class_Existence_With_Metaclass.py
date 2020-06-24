# Item 34: Register Class Existence With Metaclass
"""
1. Class registration is helpful for modular python program
2. Metaclass runs class registration each time
"""

import json
## Example 1: Naive approach
"""
The problem is that you need to know the input type in advance. `Deserialize()` needs the type.
"""
print("######### Example 1 #########")

class Serializable(object):
	def __init__(self, *args):
		self.args = args

	def serialize(self):
		return json.dumps({'args': self.args})

class Deserialize(Serializable):
	@classmethod
	def deserialize(cls, json_data):
		params = json.loads(json_data)
		return cls(*params['args'])

class Point2D(Serializable):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.x = x
		self.y = y 

	def __repr__(self):
		return f'Point2D: {self.x}, {self.y}'

class BetterPoint2D(Deserialize):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.x = x
		self.y = y 

	def __repr__(self):
		return f'Point2D: {self.x}, {self.y}'

point = Point2D(100, 200)
print(f'point: {point}')
print(f'serialize: {point.serialize()}')

point2 = BetterPoint2D(200, 300)
print(f'point: {point2}')
point2_json = point2.serialize()
print(f'serialize: {point2_json}')
point2_back = BetterPoint2D.deserialize(point2_json)
print(f'deserialize: {point2_back}')

## Example 2: A better approach.
"""
Class Type is saved. The problem is that we need to register every single of them before the usage.
"""
print("######### Example 2 #########")

class BetterSerializable(object):
	def __init__(self, *args):
		self.args = args

	def serialize(self):
		return json.dumps({"class":self.__class__.__name__, 
						   "args": self.args})

registry = {}
def register_class(target_class):
	registry[target_class.__name__] = target_class

def deserialize(data):
	params = json.loads(data)
	name = params['class']
	target_class = registry[name]
	return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Point2D: {self.x}, {self.y}'

register_class(EvenBetterPoint2D)
point3 = EvenBetterPoint2D(500, 300)
print(f'Before: {point3}')
point3_json = point3.serialize()
print(f'serialized: {point3_json}')
point3_back = deserialize(point3_json)
print(f'After: {point3_back}')

## Example 3: Metaclass
print("######### Example 3 #########")
class Meta(type):
	def __new__(meta, name, bases, class_dict):
		# print(f'meta: {meta}')
		# print(f'name: {name}')
		# print(f'bases: {bases}')
		# print(f'class_dict: {class_dict}')
		cls = type.__new__(meta, name, bases, class_dict)
		register_class(cls)
		return cls

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
	# print('1')
	pass

class Vector3D(RegisteredSerializable):
	# print('2')
	def __init__(self, x, y, z):
		super().__init__(x, y, z)
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return f'Point3D: {self.x}, {self.y}, {self.z}'

v3 = Vector3D(1, 2, 3)
print(f'Before: {v3}')
v3_json = v3.serialize()
print(f'serialized: {v3_json}')
print(f'After: {deserialize(v3_json)}')




