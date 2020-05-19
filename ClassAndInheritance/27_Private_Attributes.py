# Item 27: Prefer Public Attributes Over Private Attributes
'''
1. classmethod has access to the private attributes because the classmethod is declared within the object
2. subclass has no direct access to its parent's private fields
3. subclass can access parents' private fields by tweeking its attribute names
4. Document protected fields in parent classes
5. Only use private attributes when to avoid naming conflicts between parent and subclasses
'''

class MyObject(object):
	def __init__(self):
		self.public_field = 3
		self.__private_field1 = 'field1'
		self.__private_field2 = 'field2'

	def get_private_field1(self):
		return self.__private_field1

	def get_private_field2(self):
		return self.__private_field2

	@classmethod
	def get_private_field_of_instance(cls, instance):
		return instance.__private_field1

class MyChildObject(MyObject):
	def __init__(self):
		super().__init__()
		self._private_field1 = 'kid_field1'


foo = MyObject()
kid = MyChildObject()

## `Statement 1`
print(f'public_field: {foo.public_field}')
print(f'access from parent class: {foo.get_private_field2()}')
print(f'access from classmethod: {MyObject.get_private_field_of_instance(foo)}')

## `Statement 2`
#print(f'kid: {kid.get_private_field1()}') #should fail

## `Statement 3`
## However, because the way that python translated private attributes, private attributes are accessible
print(f'illegal acess: {kid._MyObject__private_field1}')


## Hardcoding a private attribute, which is defined in a parent class, from a subclass is bad approach because there could be another 
## layer of hierarchy added in the future. 


## 'Statement 5`
print(f'access kid private field: {kid._private_field1}')
print(f'access parent private field from parent method: {kid.get_private_field1()}')
