# Item 23: Accept Functions for Simple Interface Instead of Class
'''
1. Functions works as hooks because python has First-Class functions
2. __call__ enables a class instance to be called like a plain python function
3. stateful behavoir
'''

## Want to keep track of number of keys added

from collections import defaultdict

def log_missing():
	print('New Key Added')
	return 0

current = {'a':0, 'b':10}
increments = [('c',100), ('d', 200), ('b', 130)]

df_dict = defaultdict(log_missing, current)

print(df_dict)
for key, value in increments:
	df_dict[key] += value

print(df_dict)

## `Option 1`:  Stateful closure
def increment_with_report(increments, input_dict):
	count = 0 

	def log_missing_opt1():
		nonlocal count 
		count += 1
		return 0

	df_dict = defaultdict(log_missing_opt1, input_dict)
	for key, value in increments:
		df_dict[key] += value

	return count, df_dict

count, df_dict = increment_with_report(increments, current)
print(f'Option 1, count: {count}')

## `Option 2`: Object
class Counter():
	def __init__(self):
		self.count = 0

	def log_missing_opt2(self):
		self.count += 1
		return 0

counter = Counter()
df_dict = defaultdict(counter.log_missing_opt2, current)
for key, value in increments:
	df_dict[key] += value

print(f'Option 2, count: {counter.count}')

## `Option 3`: __call__
'''
1. Indicate the class instance will be used somewhere
2. Emphasize the primary behavior of the class
3. Emphasize the class is stateful
'''
class Counter():
	def __init__(self):
		self.count = 0

	def __call__(self):
		self.count += 1
		return 0

counter2 = Counter()
df_dict = defaultdict(counter2, current)
for key, value in increments:
	df_dict[key] += value

print(f'Option 3, count: {counter2.count}')
