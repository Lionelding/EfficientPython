# 56a: Test utils
"""
1. unitest is to test the isolated functionality within a module
2. intergration test is to test the interactions between modules
3. Inheriating TestCase for unittest
"""

from unittest import TestCase, main
from funcs_to_test import to_str

class UtilsTestCase(TestCase):

	def setUp(self):
		self.testing_str = 'hello'
		self.testing_bytes = b'hello'

	def tearDown(self):
		print('Done with Testing')

	def test_to_str_str(self):
		self.assertEqual('hello', to_str(self.testing_str))

	def test_to_str_bytes(self):
		self.assertEqual('hello', to_str(self.testing_bytes))

	def test_to_str_else(self):
		self.assertRaises(TypeError, to_str, object)

if __name__ == '__main__':
	main()

