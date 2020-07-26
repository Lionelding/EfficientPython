# Item 56: Unittest
"""
"""
def to_str(data):
	if isinstance(data, str):
		return data
	elif isinstance(data, bytes):
		return data.decode('utf-8')
	else:
		raise TypeError(f'data not supported')


# if __name__ == '__main__':
# 	main()