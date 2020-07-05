# Item 36: Multi-processing
"""
* For CPU intensive jobs, multiprocessing is faster
	Because the more CPUs, the faster 
* For IO intensive jobs, multithreading is faster
	Because the cpu needs to wait for the I/O despite how many CPUs available
	GIL is the bottleneck.


* Multi-core multi-threading is worse than single core multithreading.
* Mutli-core multi-processing is better since each process has an independent GIL

* Example 1: single process
* Example 2: multiprocess
* Example 3: multiprocess + Pool
* Example 4: multiprocess shares data with Queue


"""

import os
import time
import random
from multiprocessing import Process, Pool, cpu_count, Queue

## Example 1: single process
print("######## Example 1 ########")

def long_time_task():
	print(f'current process: {os.getpid()}')
	time.sleep(2)
	print(f"result: {8 ** 20}")


print(f'mother process: {os.getpid()}')
start = time.time()
for i in range(2):
	long_time_task()
end = time.time()
print(f'Duration: {end-start}')


## Example 2: multi-process
print("######## Example 2 ########")

def long_time_task_i(i):
	print(f'current process: {os.getpid()}, {i}')
	time.sleep(2)
	# print("result: {8 ** 20}")

print(f'mother process: {os.getpid()}')
start2 = time.time()
p1 = Process(target=long_time_task_i, args=(1, ))
p2 = Process(target=long_time_task_i, args=(2, ))

p1.start()
p2.start()
p1.join()
p2.join()

end2 = time.time()
print(f'Duration: {end2-start2}')


## Example 3: multiprocess + pool
print("######## Example 3 ########")
"""
1. process.join() needs to be after .close() and .terminate()
"""

print(f"num cpu: {cpu_count()}")
print(f'mother process: {os.getpid()}')
start3 = time.time()

pool3 = Pool(4)
for i in range(5):
	pool3.apply_async(long_time_task_i, args=(i, ))

pool3.close()
pool3.join()
end3 = time.time()

print(f'Duration: {end3-start3}')

## Example 4: Share data between multi-process using Queue
print("######## Example 4 ########")

def write(q):
	print(f'Process to write: {os.getpid()}')
	for value in ['a', 'b', 'c']:
		print(f'Put: {value}')
		q.put(value)
		time.sleep(0.2)

def read(q):
	print(f'Process to read: {os.getpid()}')
	while True:
		value = q.get(True)
		print(f'Get: {value}')

q = Queue()
pw = Process(target=write, args=(q, ))
pr = Process(target=read, args=(q, ))

pw.start()
pr.start()

pw.join()
pr.terminate()

## REF: https://zhuanlan.zhihu.com/p/46368084
## REF: https://zhuanlan.zhihu.com/p/37029560




