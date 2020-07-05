# Item 36c: Manager
"""
"""
import math
import datetime
from multiprocessing import cpu_count, Manager, Pool

print('######## Example 1 ########')
## Example 1:
def train_on_parameter(name, param, result_dict, result_lock):
    result = 0
    for num in param:
        result += math.sqrt(num * math.tanh(num) / math.log2(num) / math.log10(num))
    with result_lock:
        result_dict[name] = result
    return

start1 = datetime.datetime.now()
p = Pool(cpu_count())
print(f'Num Core: {cpu_count()}')
param_dict = {'task1': list(range(10, 30000000)),
              'task2': list(range(30000000, 60000000)),
              'task3': list(range(60000000, 90000000)),
              'task4': list(range(90000000, 120000000)),
              'task5': list(range(120000000, 150000000)),
              'task6': list(range(150000000, 180000000)),
              'task7': list(range(180000000, 210000000)),
              'task8': list(range(210000000, 240000000))}
mg = Manager()
managed_locker = mg.Lock()
managed_dict = mg.dict()

results = []
for name, param in param_dict.items():
	results.append(p.apply_async(train_on_parameter, args=(name, param, managed_dict, managed_locker)))

# results = [p.apply_async(train_on_parameter, args=(name, param, managed_dict, managed_locker)) for name, param in param_dict.items()]
results = [p.get() for p in results]
print(managed_dict)



end1 = datetime.datetime.now()
print(f'Duration: {end1 - start1}')

## REF: https://zhuanlan.zhihu.com/p/93305921



