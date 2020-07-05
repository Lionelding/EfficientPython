# Item 43: Consider `contextlib` and `with` Statement
"""
1. `with` statement allows to reuse logic from `try` and `finally`
2. `contextmanager` make it easy to use a function with the `with` statement
3. The value is yielded from the with statement is saved in `as` target
"""

import logging
from contextlib import contextmanager

print('######### Example 1 #########')
## Example 1: Reuse 'try` and `finally' with `with` statement

@contextmanager
def debug_logging(level):
	logger = logging.getLogger()
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield 
	finally:
		logger.setLevel(old_level)

def my_func():
	logging.info('	INFO message')
	logging.debug('	BUG message')
	logging.error('	ERROR message')


with debug_logging(logging.INFO):
	print('Inside')
	my_func()

print('Outside')
my_func()

print('######### Example 2 #########')
## Example 2: Save the yielded value `as` target

@contextmanager
def log_level(level, name):
	logger = logging.getLogger(name)
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield logger
	finally:
		logger.setLevel(old_level)

with log_level(logging.DEBUG, 'mylogger') as logger:
	logger.debug('Shows this message')
	logging.debug('Not show this message')

logger2 = logging.getLogger('mylogger2')
logger2.debug('Will not display this')

