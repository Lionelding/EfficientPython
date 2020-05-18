# Item 25: Always Use super to Inherit the parent class
'''
1. Method Resolution Order --> __class__.mro()
2. Using super().__init__ and MRO resolve the diamond inheritance issue
'''

# `Diamond Inheritance Issue`
'''
self.value is reset back to 5
'''

from pprint import pprint

class MyBaseClass(object):
	def __init__(self, value):
		self.value = value

class TimesFive(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value *= 5

class PlusTwo(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value += 2

class ThisWay(TimesFive, PlusTwo):
	def __init__(self, value):
		TimesFive.__init__(self, value)
		PlusTwo.__init__(self, value)

print(ThisWay(5).value) 

## With super 

class TimesFiveCorrect(MyBaseClass):
	def __init__(self, value):
		super().__init__(value)
		self.value *= 5

class PlusTwoCorrect(MyBaseClass):
	def __init__(self, value):
		super().__init__(value)
		self.value += 2

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
	def __init__(self, value):
		super().__init__(value)

print(GoodWay(5).value)
pprint(GoodWay.mro())