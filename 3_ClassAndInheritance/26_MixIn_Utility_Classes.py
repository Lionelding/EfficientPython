# Item 26: Mix-in Utility Classes
'''
1. mix-in is small class that only defines a set of additional methods
2. mix-in has no __init__ and instance attributes
3. At instance level, provide per-class customization when mix-in classes may require it
'''

## Convert an object to dictionary


import json
from pprint import pprint


## `Advantage 1`: Dynamic Inspection and generic functionality

class ToDictMixin(object):
	def to_dict(self):
		return self._traverse_dict(self.__dict__)
		
	def _traverse_dict(self, instance_dict):
		output = {}
		for key, value in instance_dict.items():
			output[key] = self._traverse(key, value)
		return output

	def _traverse(self, key, value):
		if isinstance(value, ToDictMixin):
			return value.to_dict()
		elif isinstance(value, dict):
			return self._travese_dict(value)
		elif isinstance(value, list):
			return [self._travse(i) for i in value]
		elif hasattr(value, '__dict__'):
			return self._travese_dict(value.__dict__)
		else:
			return value

class BinaryTree(ToDictMixin):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

tree = BinaryTree(10, 
	left=BinaryTree(7, right=BinaryTree(9)),
	right=BinaryTree(13, left=BinaryTree(11)))

pprint(tree.to_dict())

class BinaryTreeWithParent(BinaryTree):
	def __init__(self, value, left=None, right=None, parent=None):
		super().__init__(value, left, right)
		self.parent = parent

	def _traverse(self, key, value):
		# Prevent Cycles
		if (isinstance(value, BinaryTreeWithParent) and key == 'parent'):
			return value.value
		else:
			return super()._traverse(key, value)


root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
pprint(root.to_dict())

## `Advantage 2`: Mixin can be composed together

class JsonMixin(object):
	@classmethod
	def from_json(cls, data):
		kwargs = json.loads(data)
		return cls(**kwargs)

	def to_json(self):
		return json.dumps(self.to_dict())
