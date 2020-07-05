# Item 41: Consider concurrent futures
"""
"""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

print('######### Example 1 #########')
## Example 1:
def gcd(pair):
	a, b = pair
	low = min(a, b)
	for i in range(low, 0, -1):
		if a % i ==0 and b % i ==0:
			return i


numbers = [(12411, 1241241), (552112, 1240124), (5124123, 8917500)]
start1 = time.time()
results = list(map(gcd, numbers))
end1 = time.time()
print(f'Duriation: {end1 - start1}')

start2 = time.time()
pool = ThreadPoolExecutor(max_workers=4)
results = list(pool.map(gcd, numbers))
end2 =time.time()
print(f'Duriation: {end2 - start2}')

start3 = time.time()
pool = ProcessPoolExecutor(max_workers=4)
results = list(pool.map(gcd, numbers))
end3 =time.time()
print(f'Duriation: {end3 - start3}')
