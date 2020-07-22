# Item 59: Use tracemalloc to Understand Memory Usage and Leaks
"""
1. Allocate and check the memory usage in Python
"""

class Fake:
	def __init__(self):
		self.attributes = []


print("######### Example 1 #########")
## Example 1: `gc` tells which object exists, but no information about how they were allocated

import gc
found_objects = gc.get_objects()
print(len(found_objects))

lol1 = Fake()
lol2 = Fake()
lol3 = Fake()
lol4 = Fake()
lol5 = Fake()


found_objects = gc.get_objects()
print(len(found_objects))
for obj in found_objects[-3:]:
	print(repr(obj)[:100])

print("######### Example 2 #########")
## Example 2: `tracemalloc` lists the source of memory usage

import tracemalloc
tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()
lol10 = Fake()
lol20 = Fake()
lol30 = Fake()
lol40 = Fake()
lol50 = Fake()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
	print(stat)

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print(top.traceback.format())
