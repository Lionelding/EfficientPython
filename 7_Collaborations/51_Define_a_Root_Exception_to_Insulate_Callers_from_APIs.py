# Item 51: Define a Root Exception to Insulate Caller from APIs
"""
1. Base, Intermediate, Specifci Exceptions to handle errors in different levels
"""

import logging

logger = logging.getLogger()

class Error(Exception):
	"""Base-Class for all customized Exceptions"""
	def __init__(self, message='There is a bug somewhere'):
		self.message = message
		super().__init__(self.message)

class InvalidXError(Error):
	def __init__(self):
		self.message = 'An error with x'
		super().__init__(self.message)

class InvalidYError(Error):
	def __init__(self):
		self.message = 'An error with y'
		super().__init__(self.message)

def compute_some_result(x, y):

	result = 0

	if x<= 0:
		raise InvalidXError()
	if y>= 0:
		raise InvalidYError() 
	if result == 0:
		raise Error()


try:
	compute_some_result(8, -1)
except InvalidXError as e:
	logger.error(e)
except Error as e:
	logger.error(e)
