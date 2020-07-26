# Item 58: Profile Before Optimizing
"""
1. Use cProfile insteal of Profile
2. profilr.runcall() for running analyzsis
3. Stats object for visualizing
"""
from pstats import Stats
from cProfile import Profile
from bisect import bisect_left

def insert_value(array, value):
	i = bisect_left(array, value)
	array.insert(i, value)


# def insert_value(array, value):
# 	for i, existing in enumerate(array):
# 		if existing > value:
# 			array.insert(i, value)
# 			return 
# 	array.append(value)


def insertion_sort(data):
	result = []
	for value in data:
		insert_value(result, data)
	return result


from random import randint
max_size = 10**3
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

profiler = Profile()
profiler.runcall(test)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()