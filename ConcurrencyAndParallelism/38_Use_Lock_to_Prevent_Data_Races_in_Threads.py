# Item 38: Use Lock to Prevent Data Races in Threads
"""
1. GIL would interupt a current thread anytime because it tries to enforce fairness between all threads.
2. Data structure would be corrupted if multiple threads modifies the same object
3. Use `Lock`, which is mutual exclusion, to protect the shared object.
"""
# Setup
from threading import Thread, Lock

print('######### Example 1 #########')
## Example 1: 
class Counter(object):
	def __init__(self):
		self.lock = Lock()
		self.count = 0

	def increment(self, offset):
		with self.lock:
			self.count = self.count + offset

		## value = getattr(counter, 'count')
		## result = value + offset
		## setattr(counter, 'count', result)

def worker(sensor_idx, how_many, counter):
	for _ in range(how_many):
		counter.increment(1)

def run_threads(func, how_many, counter):
	threads = []
	for i in range(5):
		args = (i, how_many, counter)
		thread = Thread(target=func, args=args)
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()

how_many = 10**5
counter = Counter()
run_threads(worker, how_many, counter)
print(f'Counter should be  {5*how_many}, but is {counter.count}')