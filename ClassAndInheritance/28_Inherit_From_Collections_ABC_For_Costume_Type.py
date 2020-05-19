# Item 28: Inherit from collections abc for Costume Container Type
'''
1. Defining a custom container, which has some typical functions, is hard especilly
2. When required methods are implemented, the additional methods will be provided for free.
'''
from collections.abc import Sequence

class BinaryNode(Sequence):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __getitem__(self):
		pass

	def __len__(self):
		pass


