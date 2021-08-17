# Item 25a: super 
"""
Why do we need `super`?
1. So that child classes in Cooperative Multiple Inheritance will call the correct next parent class function in MRO
because `super()` enabls indirection with forward compatibility
	REF: https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
	REF: https://stackoverflow.com/a/33469090/541136

2. `super()` for multiple inheritance: When every class uses super().__init__()

In details:
3. For unrelated, and standalone classes
	In the child class, multiple `super()` needs to be called to inherit each of its parent class. 
	The order of calling `super()` should be consistent with the parent class order

4. For coorporative, related classes
	In terms of order, before the run-time, it is not clear which class `super()` will pass its parameters to.
	It could pass to its sibling class, or to its parent depending on these classes inheritance.
	Therefore, it would be easier if the parent or sibling class takes `**kwargs` as input

	REF: https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way/50465583#50465583
"""

print("######### Example 1 #########")
## Example 1: Indirection with Forward Compatibility
## You may not need that functionality, but subclassers of your code may

class SomeBaseClass(object):
	def __init__(self):
		print('SomeBaseClass.__init__(self) called')

class UnsuperChild(SomeBaseClass):
	def __init__(self):
		print('UnsuperChild.__init__(self) called')
		SomeBaseClass.__init__(self)

class SuperChild(SomeBaseClass):
	def __init__(self):
		print('SuperChild.__init__(self) called')
		super().__init__()

class InjectMe(SomeBaseClass):
	def __init__(self):
		print('InjectMe.__init__(self) called')
		super().__init__()

## `UnsuperInjector` fails to inject the dependency 
## because `UnsuperChild` has hard-coded the method to be called after its own
class UnsuperInjector(UnsuperChild, InjectMe): pass

## `SuperInjector` correctly injects the dependency
## because `SuperChild` uses super() to handle
class SuperInjector(SuperChild, InjectMe): pass

o1 = UnsuperChild()
print('')
o2 = SuperInjector()

## The `UnsuperChild` does not have access to InjectMe. 
## It is the `UnsuperInjector` that has access to `InjectMe`
##  - and yet cannot call that class's method from `UnsuperChild`.

## Both `UnsuperInjector` and `SuperInjector` intend to call a method by the same name that comes next in the MRO.

## The one without `super` hard-codes its parent's method
## thus is has restricted the behavior of its method, and subclasses cannot inject functionality in the call chain.

## The one with super has greater flexibility. 
## The call chain for the methods can be intercepted and functionality injected.



print("######### Example 2 #########")
# Example 2: 
class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')

print('')
print(f'Method Resolution Order: {Dog.__mro__}')

print("######### Example 3 #########")
# Example 3: For unrelated, and standalone classes

class Foo:
    def __init__(self, foo):
        self.foo = foo

class Bar:
    def __init__(self, bar):
        self.bar = bar

class Sha:
    def __init__(self, sha):
        self.sha = sha

class FooBarSha(Foo, Bar, Sha):
	def __init__(self, bar='bar'):
		super().__init__('foo')
		super(Foo, self).__init__('bar')
		super(Bar, self).__init__('sha')

foobar = FooBarSha()
print(foobar.__dict__)


print("######### Example 4 #########")
# Example 4: For coorporative, related classes

class CoopFoo:
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.foo = kwargs['value']

class CoopBar:
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.bar = kwargs['value']

class CoopSha:
	def __init__(self, value, **kwargs):
		super().__init__(**kwargs)
		self.sha = value

class CoopFooBarSha(CoopFoo, CoopBar, CoopSha):
	def __init__(self, value='a'):
		super().__init__(value=value)

coopfoobarsha = CoopFooBarSha()
print(coopfoobarsha.__dict__)


