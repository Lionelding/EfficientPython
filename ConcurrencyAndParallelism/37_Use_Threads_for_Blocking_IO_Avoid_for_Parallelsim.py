# Item 37: Use Threads for Blocking IO, Avoid for Parallelism
"""
Python threads can not run bytecode in parallel on multiple CPU resources because of GIL
Why supporting multi-thread despite GIL
1. Multiple functions seemingly in parallel
2. To deal with the blocking IO, especially during the system call.
"""

# Setup
import select, socket
from datetime import datetime, time
from threading import Thread

print('######### Example 1 #########')
## Example 1: No true multi-threading

def factorize(number):
	for i in range(1, number + 1):
		if number % i == 0:
			# print(i)
			yield i


numbers = [2139079, 123133, 1125125, 1852285]

start = datetime.now()
for number in numbers:
	list(factorize(number))

end = datetime.now()
print(f'Duration: {end - start}')

class FactorizeThread(Thread):
	def __init__(self, number):
		super().__init__()
		self.number = number

	def run(self):
		self.factors = list(factorize(self.number))

start2 = datetime.now()
threads = []
for number in numbers:
	thread = FactorizeThread(number)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

end2 = datetime.now()
print(f'Duration: {end2-start2}')

print('######### Example 2 #########')
## Example 2: 

def slow_systemcall():
	select.select([socket.socket()], [], [], 0.2)

### Make a system call in sequence
start3 = datetime.now()
for _ in range(5):
	slow_systemcall()
end3 = datetime.now()
print(f'Duration: {end3-start3}')

### Make a system call in Parallel
"""
Python threads release GIL before making system calls, and reacquire the GIL after the system call
"""
start4 = datetime.now()
print(start4)
threads = []
for _ in range(5):
	thread = Thread(target=slow_systemcall())
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()
end4 = datetime.now()
print(end4)

print(f'Duration: {end4-start4}')

