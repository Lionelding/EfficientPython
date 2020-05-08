# item 20: Use None and Docstring to specify dynamic values
'''
	1. Default arguments are evaluated once during the function evaluation at the model load time.
	2. Use None as the keyword arguments if they have dynamic values. Use Docstring to specify the behavior
'''
import json
import time
import datetime


## `Bad example 1`: Default values are evaluated only once per module load
def log(message, when=datetime.datetime.now()):
	print('{} {} '.format(when, message))
	return 

log('A')
time.sleep(0.1)
log('B')

## `Good example 1`: Use None for the default values when they are mutable
def log(message, when=None):
	when = datetime.datetime.now()
	print('{} {} '.format(when, message))
	return 

log('C')
time.sleep(0.1)
log('D')

## `Bad example 2`: the default dictionary is the same object across two calls
def decode(data, default={}):
	try:
		return json.loads(data)
	except ValueError:
		return default

txt1 = decode('What the hell1')
txt2 = decode('What the hell2')
txt1['AA'] = 11
txt2['BB'] = 22
print(txt1)
print(txt2)

assert txt1 is txt2


## `Good example 2`: Use None for the default values when they are mutable
def decode(data, default=None):
	default = {}
	try:
		return json.loads(data)
	except ValueError:
		return default

txt1 = decode('What the hell1')
txt2 = decode('What the hell2')
txt1['AA'] = 11
txt2['BB'] = 22
print(txt1)
print(txt2)

