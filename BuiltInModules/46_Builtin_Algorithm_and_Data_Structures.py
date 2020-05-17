# Item 46: Built-in Algorithm and Data Structures
'''
1. Double-ended Queue
2. Ordered Dictionary
3. Default Dictionary
4. Heap queue
5. Bisection
5. Iterator tools
'''

## `Double-ended Queue`
from collections import deque

fifo = deque()
fifo.append(1)
fifo.append(2)
print(f'fifo {fifo}')
print(fifo.popleft())
print(f'fifo {fifo}')

## `Ordered Dictionary`
'''
Standard dictionary are not ordered
'''
from collections import OrderedDict

a = OrderedDict()
a['first_a']=1
a['second_a']=2
a['third_a']=3

b = {}
b['first_b']=1
b['second_b']=2
b['third_b']=3
for value_a, value_b in zip(a.values(), b.values()):
	print(f'{value_a}, {value_b}')

## `Default Dictionary`
'''
Automatically store a default value when a key dose not exist
'''
from collections import defaultdict

def create_default_value():
	print('Key Added')
	return 100

stats = {'a':1, 'b':2}
stats_init = defaultdict(create_default_value, stats)
stats_init['x'] += 5
print(stats_init)
print(stats_init['c'])

## `Heap Queue`
'''
Items are always removed by the highest priority (lowest number).
Each heapq operations take logrithmic time in proportion to the lenght of the list.
'''
from heapq import heappush, heappop, nsmallest
h = []
heappush(h, 3)
heappush(h, 5)
heappush(h, 0)
heappush(h, -1)

print(h)
print(nsmallest(1, h))
assert h[0]==nsmallest(1, h)[0]
print(heappop(h), heappop(h), heappop(h), heappop(h))

## `Bisection`
'''
Need a SORTED list
'''
from bisect import bisect_left
import datetime

long_list = list(range(10**8))
time_a = datetime.datetime.now()
i = long_list.index(991230)
print(f'Time spent: {datetime.datetime.now() - time_a}')

i = bisect_left(long_list, 991230)
print(f'Time spent with bisect_left: {datetime.datetime.now() - time_a}')

