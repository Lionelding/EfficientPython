# Item 21: Enfore the clarity with Keyword-only Arguments
'''
1. It is easy to confuse with positional arguments
2. Use keyword-only argumentss to force callers to supply keyword arguments for potentially confusing functions.
'''

## `Bad example 1`: Easy to confuse with positional argumentions. 
def compute_the_math(number, divisor, igore_overflow, ignore_zero_division):
 	try:
 		return number / divisor
 	except OverflowError:
 		if igore_overflow:
 			return 0
 		else:
 			raise
 	except ZeroDivisionError:
 		if ignore_zero_division:
 			return float('inf')
 		else:
 			raise


print(compute_the_math(10, 0, False, True))

## `Good example 1`: Force to accept keyword arguments only
## The * indicts the end of positional arguments, and beginning of the keyword-only arguments
def compute_the_math(number, divisor, *, igore_overflow=False, ignore_zero_division=False):
 	try:
 		return number / divisor
 	except OverflowError:
 		if igore_overflow:
 			return 0
 		else:
 			raise
 	except ZeroDivisionError:
 		if ignore_zero_division:
 			return float('inf')
 		else:
 			raise


#print(compute_the_math(10, 0, False, True)) # Fail
print(compute_the_math(10, 0, ignore_zero_division=True))