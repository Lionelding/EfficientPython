# Item 36b: Multi-threading
"""
* Example 1: Multithreading
* Example 2: Program stops when the main thread exits
* Example 3: Customer Wrapper
* Example 4: Multithreading share resources with Queue
"""

import time
import threading
from threading import Thread
from queue import Queue


## Example 1: multithreading
print("######### Example 1 #########")

def long_time_task_i(i):
	print(f'current thread: {threading.current_thread().name}, {i}')
	time.sleep(2)
	print(f'result: {8 ** 20}')

start1 = time.time()
print(f'main process: {threading.current_thread().name}')

t1 = Thread(target=long_time_task_i, args=(1, ))
t2 = Thread(target=long_time_task_i, args=(2, ))
t1.start()
t2.start()

t1.join()
t2.join()

end1 = time.time()
print(f'Duration: {end1 - start1}')

## Example 2: Program stops when the main thread exits
print("######### Example 2 #########")
"""
All of the child threads stop when the main thread exits
"""

start2 = time.time()
print(f'main process: {threading.current_thread().name}')
for i in range(5):
	t = Thread(target=long_time_task_i, args=(i, ))
	t.setDaemon(True)
	t.start()

end2 = time.time()
print(f'Duration: {end2 - start2}')

## Example 3: Customer Wrapper
print("######### Example 3 #########")

def long_time_task(i):
	time.sleep(2)
	return 8 ** 20

class MyThread(Thread):
	def __init__(self, func, args, name=''):
		super().__init__()
		self.func = func
		self.args = args
		self.name = name
		self.result = None

	def run(self):
		print(f'start thread: {self.name}')
		self.result = self.func(self.args[0])
		print(f'result: {self.result}')
		print(f'finish thread: {self.name}')


start3 = time.time()
threads = []
for i in range(1, 3):
	t = MyThread(long_time_task, (i, ), str(i))
	threads.append(t)

for t in threads:
	t.start()

for t in threads:
	t.join()

end3 = time.time()
print(f'Duration: {end3 - start3}')

print("######### Example 4 #########")
## Example 4: Multithreading share resources with Queue
"""
Queue.empty() and .full() are not that reliable.
"""

class Producer(Thread):
	def __init__(self, name, queue):
		super().__init__(name=name)
		self.queue = queue

	def run(self):
		for i in range(1, 5):
			print(f'{self.getName()} puts {i} to the queue')
			self.queue.put(i)
			time.sleep(2)
		print(f'{self.getName()} finishes')

class Consumer(Thread):
	def __init__(self, name, queue):
		super().__init__(name=name)
		self.queue = queue

	def run(self):
		for i in range(1, 5):
			print(f'{self.getName()} gets {i} from the queue')
			result = self.queue.get()
			time.sleep(2)

		print(f'{self.getName()} finishes')

queue = Queue()
producer = Producer('Producer', queue)
consumer = Consumer('Consumer', queue)

producer.start()
consumer.start()

producer.join()
consumer.join()

print('FINISHED')


