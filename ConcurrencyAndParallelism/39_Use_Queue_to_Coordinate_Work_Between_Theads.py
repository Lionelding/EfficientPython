# Item 39: Use Queue to Coordinate Work Between Threads
"""
Problems witht this implementation
1. Busy waiting
2. stopping worker
3. Memory explosion
"""
import time
from threading import Thread, Lock
from collections import deque

def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item

class MyQueue(object):
	def __init__(self):
		self.items = deque()
		self.lock = Lock() 

	def put(self, item):
		with self.lock:
			self.items.append(item)

	def get(self):
		with self.lock:
			return self.items.popleft()

class Worker(Thread):
	def __init__(self, func, in_queue, out_queue):
		super().__init__()
		self.func = func
		self.in_queue = in_queue
		self.out_queue = out_queue
		self.polled_count = 0
		self.work_done = 0

	def run(self):
		while True:
			self.polled_count += 1
			try:
				item = self.in_queue.get()
			except IndexError:
				time.sleep(0.01)
			except AttributeError:
				return
			else:
				result = self.func(item)
				self.out_queue.put(result)
				# print(len(self.out_queue.items))
				self.work_done += 1

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()

threads = [Worker(download, download_queue, resize_queue), 
		   Worker(resize, resize_queue, upload_queue),
		   Worker(upload, upload_queue, done_queue)]

for thread in threads:
	thread.start()

for _ in range(1000):
	download_queue.put(object())

while len(done_queue.items) < 1000:
    time.sleep(0.1)

for thread in threads:
	thread.in_queue = None
	thread.join()

processed = len(done_queue.items)
polled = sum(thread.polled_count for thread in threads)
print(f'processed: {processed}, polled: {polled}')
