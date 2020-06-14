# Item 29: Use Plain Attributes Instead of Get and Set Methods
'''
1. Avoid to define set() and get() explictly
2. With decorator, both setter and getter need to match the attribute name
3. Use setter to validate input type or value
4. Make attribute immutable
5. class.__init__() --> @property.setter,  before an object in constructured
6. Attributes can only be shared with subclass.
7. Don't set other attributes inside getter 
'''

class Resistor(object):
	def __init__(self, ohms):
		self.ohms = ohms
		self.voltage = 0.0
		self.current = 0
	
r1 = Resistor(10)
r1.ohms = 100
print(f'r1 ohms is {r1.ohms}')

# `Statement 2` 
class VoltageResistance(Resistor):
	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage
		self.current = self._voltage / self.ohms

r2 = VoltageResistance(100)
print(f'Before, r2 voltage: {r2.voltage}, r2 current: {r2.current}')
r2.voltage = 2500
print(f'After, r2 voltage: {r2.voltage}, r2 current: {r2.current}')

# 'Statement 3'
class BoundedResistance(Resistor):
	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if ohms <= 0:
			raise ValueError(f'Erorr: {ohms} ohms is <= 0')
		self._ohms = ohms
	
r3 = BoundedResistance(1e3)
print(f'r3 ohms: {r3.ohms}')
# r3.ohms = 0 # Error

# 'Statement 4'
class FixedResistance(Resistor):
	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if hasattr(self, '_ohms'):
			raise AttributeError("Already have this attribute")
		self._ohms = ohms

r4 = FixedResistance(200)
print(f'r4 ohms: {r4.ohms}')
# r4.ohms = 300 # Error

