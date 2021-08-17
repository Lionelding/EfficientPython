# Item 24: Use classmethod Polymorphism to Construct Object Genenrically
'''
1. Use classmethod to define an alternative constructor for a class
'''
import os
from threading import Thread

class InputData(object):
	def read(self):
		raise NotImplementedError


class PathInputData(InputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path, encoding="utf-8").read()


class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError

class LineCountWorker(Worker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result = other.result + self.result


## `Option 1`: Manually Orchestrate everything
'''
The function `mapreduce` is not generic at all. 
'''
def generate_inputs(data_dir):
	for name in os.listdir(data_dir):
		print(f'File: {name}')
		yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
	workers = []
	print(input_list)
	for input_data in input_list:
		workers.append(LineCountWorker(input_data))
	return workers

def execute(workers):
	threads = [Thread(target=w.map) for w in workers]
	for thread in threads: thread.start()
	for thread in threads: thread.join()

	first, rest = workers[0], workers[1:]
	for worker in rest:
		first.reduce(worker)

	return first.result

def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers = create_workers(inputs)
	return execute(workers)

result = mapreduce('../testdata')
print(f'result1: {result}')


## `Option 2`: Using classmethod
class GenericInputData(object):

	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		raise NotImplementedError

	@classmethod
	def generate_inputs(cls, config):
		raise NotImplementedError

class PathInputData(GenericInputData):

	def read(self):
		return open(self.path, encoding="utf-8").read()

	@classmethod
	def generate_inputs(cls, config):
		data_dir = config['data_dir']
		for name in os.listdir(data_dir):
			yield cls(os.path.join(data_dir, name))

class GenericWorker(object):

	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError

	@classmethod
	def create_workers(cls, input_class, config):
		workers = []
		for input_data in input_class.generate_inputs(config):
			workers.append(cls(input_data))
		return workers

class LineCountWorker(GenericWorker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result = other.result + self.result

def mapreduce(worker_class, input_class, config):
	workers = worker_class.create_workers(input_class, config)
	return execute(workers)

result2 = mapreduce(LineCountWorker, PathInputData, {'data_dir':'../testdata'})
print(f'result2: {result2}')