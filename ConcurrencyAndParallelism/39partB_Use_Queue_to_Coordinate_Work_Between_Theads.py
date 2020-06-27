# Item 39 Part b: Use Queue to Coordinate Work Between Threads 
"""
1. Queue eliminate busy waiting by blocking operation
2. Queue has a buffer size, and can implement __iter__ for memory explosion
3. Stop worker: queue.task_done() and queue.join()
"""
# Setup
import time
from queue import Queue
from threading import Thread, Lock

print("######### Example 1 #########")
## Example 1: Block operation
queue1 = Queue()

def consumer():
	print('Consumer Waiting')
	queue1.get()
	print('Consumer Done')

thread = Thread(target=consumer)
thread.start()


print('Producer Waiting')
queue1.put(object())
thread.join()
print('Producer Done')

print("######### Example 2 #########")
## Example 2: a queue with a buffer size

queue2 = Queue(1)
def consumer2():
	time.sleep(0.1)
	queue2.get()
	print('Consumer got 1')
	queue2.get()
	print('Consumer got 2')

thread = Thread(target=consumer2)
thread.start()

queue2.put(object())
print('Producing put 1')
queue2.put(object())
print('Producing put 2')
thread.join()
print('Producer done')

print("######### Example 3 #########")
## Example 3: queue.task_done() and queue.join()

queue3 = Queue()
def consumer3():
	print('Consumer Waiting')
	work = queue3.get()
	print('Consumer Working')
	time.sleep(0.1)
	print('Consumer Done')
	queue3.task_done()

thread = Thread(target=consumer3)
thread.start()

queue3.put(object())
print('Producer Waiting')
queue3.join()

print("######### Example 4 #########")
## Example 4: Combined

def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item

class ClosableQueue(Queue):
	SENTINEL = object()

	def close(self):
		self.put(self.SENTINEL)

	### Define an iterator
	def __iter__(self):
		while True:
			item = self.get()
			try:
				if item is self.SENTINEL:
					return 
				yield item
			finally:
				self.task_done()

class StoppableWorker(Thread):
	def __init__(self, func, in_queue, out_queue):
		super().__init__()
		self.func = func
		self.in_queue = in_queue
		self.out_queue = out_queue

	def run(self):
		for item in self.in_queue:
			result = self.func(item)
			self.out_queue.put(result)

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [StoppableWorker(download, download_queue, resize_queue), 
		   StoppableWorker(resize, resize_queue, upload_queue),
		   StoppableWorker(upload, upload_queue, done_queue)]

for thread in threads:
	thread.start()

for _ in range(1000):
	download_queue.put(object())

download_queue.close()
download_queue.join()

resize_queue.close()
resize_queue.join()

upload_queue.close()
upload_queue.join()

print(done_queue.qsize())	
