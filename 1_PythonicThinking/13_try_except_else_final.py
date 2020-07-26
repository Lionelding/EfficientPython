# Item 13: Take Advantage of Try/Except/Else/Finally
"""
1. try + finally enable code cleaning
2. `else` block help minimize the amount of the code in `try`, and visually distinguish the success case from `try/except`
"""
import json

print('######### Example 1 #########')
# Example 1: try + finally
handle = open("../testdata/Speech1.txt", 'r+', encoding="utf-8")
# handle = open(file_path, 'r+', encoding="utf-8")
try: 
	data = handle.read()

finally:
	## Happens anyway except the IO problem 
	handle.close()

print('######### Example 2 #########')
# Example 2: try + except + else

def load_json_key(data, key):
	try:
		result_dict = json.loads(data)
	except ValueError as e:
		raise KeyError from e
	else:
		## When the try block does not raise an exception, the `else` block will run
		return result_dict[key]


print('######### Example 3 #########')
# Example 3: try + except + else + finally

UNDEFINED = object()
def divide_json(path):
	handle = open(path, 'r+') # May raise IOError
	try:
		data = handle.read()  # May raise UnicodeDecodeError
		op = json.loads(data) # May raise ValueErorr
		value = (
			op['numerator'] / 
			op['denominator'])# May raises ZeroDivisionError
	except ZeroDivisionError as e:
		return UNDEFINED
	else:
		op['result'] = value
		result = json.dumps(op)
		handle.seek(0)
		handle.write(result)  # May raise IOError
		return value
	finally:
		handle.close()		  # Always run
