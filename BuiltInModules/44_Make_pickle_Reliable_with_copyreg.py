# Item 44: Make pickle Reliable with copyreg
"""
1. `pickle` built-in modele is only useful between trusted programs. 
   The serailized data contains information about how to reconstruct an originial object. 
   A malicious program can be used to compromise other programs when they attempt to deserailize it.
2. Use `copyreg.pickle` to solve default value missing issue
3. use `copyreg.pickle` to version classes for the backward-incompatible changes.
4. use `copyreg.pickle` for stable import path.
"""

import copy
import pickle
import copyreg

print('######### Example 1 #########')
## Example 1: Pickle file dumps/loads an object regardless of its attributes. 
## 			  Potentially create conflicts between different verison of instances such as attribute missing

class GameState(object):
	def __init__(self):
		self.level = 0
		self.lives = 4
		self.points = 0

state1 =GameState()
state1.level += 1
state1.lives -= 1

state_path = 'game_state.bin'
with open(state_path, 'wb') as f:
	pickle.dump(state1, f)

with open(state_path, 'rb') as f:
	state1_resumed = pickle.load(f)
print(state1_resumed.__dict__)

assert isinstance(state1_resumed, GameState)


print('######### Example 1.5 #########')
## Example 1.5: copyreg
"""
copyreg.pickle(type, function, constructor=None)¶
Declares that function should be used as a “reduction” function for objects of type `type`. 
`function` should return either a string or a tuple containing two or three elements. 
The first returned element from the `function` must be callable. 

The optional constructor parameter, if provided, is a callable object which can be used
to reconstruct the object when called with the tuple of arguments returned by function at pickling time. 
TypeError will be raised if object is a class or constructor is not callable.
"""

class C(object):
	def __init__(self, a):
		self.a = a

def unpickle_c(kwargs):
	print('Unpickling C')
	return C(**kwargs)

def pickle_c(c):
	kwargs = c.__dict__
	print(f'Pickling C with kwargs: {kwargs}')
	return unpickle_c, (kwargs,)

copyreg.pickle(C, pickle_c)
c = C(1)
c_serailized = pickle.dumps(c)

print('Reconstruction ...')
c_resumed = pickle.loads(c_serailized)
print(c_resumed.__dict__)

print('######### Example 2 #########')
## Example 2: Default Attribute Values

class GameState(object):
	def __init__(self, level=0, lives=0, points=0):
		self.level = level
		self.lives = lives
		self.points = points

def unpickle_game_state(kwargs):
	return GameState(**kwargs)

def pickle_game_state(game_state):
	print('Pickling GameState')
	kwargs = game_state.__dict__
	return unpickle_game_state, (kwargs,)

copyreg.pickle(GameState, pickle_game_state)
state2 = GameState()
state2.points += 1000
serialized = pickle.dumps(state2)
print('Reconstruction ...')
state2_resumed = pickle.loads(serialized)
print(state2_resumed.__dict__)


class GameState(object):
	def __init__(self, level=0, lives=0, points=0, magic=5):
		self.level = level
		self.lives = lives
		self.points = points
		self.magic = magic

state2_after = pickle.loads(serialized)
print(state2_after.__dict__)


print('######### Example 3 #########')
## Example 3: Versioning Classes

class GameState(object):
	def __init__(self, level=0, points=0, magic=5):
		self.level = level
		self.points = points
		self.magic = magic
try:
	pickle.loads(serialized)

except TypeError as e:
	print(f'Failed: {e}')

def unpickle_game_state(kwargs):
	version = kwargs.pop('version', 1)
	if version == 1:
		kwargs.pop('lives')
	return GameState(**kwargs)

def pickle_game_state(game_state):
	kwargs = game_state.__dict__
	kwargs['version'] = 2
	return unpickle_game_state, (kwargs,)

copyreg.pickle(GameState, pickle_game_state)
state3_after = pickle.loads(serialized)
print(state3_after.__dict__)

print('######### Example 4 #########')
## Example 4: Versioning Classes
class BetterGameState(object):
	def __init__(self, level=0, points=0, magic=5):
		self.level = level
		self.points = points
		self.magic = magic

pickle.loads(serialized)
print(serialized[:35])

copyreg.pickle(BetterGameState, pickle_game_state)
state4 = BetterGameState()
state4_serialized = pickle.dumps(state4)
print(state4_serialized[:35])


