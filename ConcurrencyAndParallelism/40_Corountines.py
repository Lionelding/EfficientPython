# Item 40: Corountines
"""
1. yield == iteractively return + receive
2. Within a generator, the value of the yeild expression will 
   be whatever value was passed to the generator's `send` method from the exterior code
3. Corountine can run many functions `seemingly` at the same time.
4. `yield from` composes generator coroutins together
"""
from collections import namedtuple

print("######### Example 1 #########")
## Example 1:
def my_coroutine():
	while True:
		received = yield
		print(f'received: {received}')

it = my_coroutine()
next(it)
it.send('item 1')
it.send('item 2')

def minimize():
	current = yield
	print(f'current: {current}')
	while True:
		value = yield current
		print(f'value: {value}')
		current = min(value, current)

itit = minimize()
next(itit)
print(itit.send(10))
print(itit.send(4))
print(itit.send(10))
print(itit.send(-10))

print("######### Example 2 #########")
## Example 2: Game of Life Implementation

Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
TICK = object()
ALIVE = '*'
EMPTY = '_'

def count_neighbors(y, x):
	n_ = yield Query(y+1, x+0)
	ne = yield Query(y+1, x+1)
	e_ = yield Query(y+0, x+1)
	se = yield Query(y-1, x+1)
	s_ = yield Query(y-1, x+0)
	sw = yield Query(y-1, x-1)
	w_ = yield Query(y+0, x-1)
	nw = yield Query(y+1, x-1)
	neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
	count = 0
	for state in neighbor_states:
		if state == 'ALIVE':
			count = count + 1
	return count

# Testcase 1
# it = count_neighbors(10, 5)
# q = next(it)

# for i in range(8):
# 	print(f'q{i}')
# 	try:
# 		q = it.send('ALIVE')
# 	except StopIteration as e:
# 		print(f'Count: {e.value}')

def game_logic(state, neighbors):
	if state == ALIVE:
		if neighbors < 2:
			return EMPTY
		elif neighbors > 3:
			return EMPTY
	else:
		if neighbors == 3:
			return ALIVE

	return state


def step_cell(y, x):
	state = yield Query(y, x)
	neighbors = yield from count_neighbors(y, x)
	next_state = game_logic(state, neighbors)
	yield Transition(y, x, next_state)

# Testcase 2:
# it = step_cell(10, 5)
# q0 = next(it)
# print(f'Me: {q0}')
# for i in range(8):
# 	it.send('ALIVE')
# t = it.send('ALIVE')
# print(f'outcome: {t}')

def simulate(height, width):
	while True:
		for y in range(height):
			for x in range(width):
				yield from step_cell(y, x)
			yield TICK

class Grid(object):
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.rows = []
		for _ in range(self.height):
			self.rows.append([EMPTY] * self.width)

	def __str__(self):
		lol = ''
		for r in self.rows:
			line = ''.join(r)
			lol = lol + line + '\n'
		return lol

	def query(self, y, x):
		return self.rows[y % self.height][x % self.width]

	def assign(self, y, x, state):
		self.rows[y % self.height][x % self.width] = state

def live_a_generation(grid, sim):
	progeny = Grid(grid.height, grid.width)
	item = next(sim)
	while item is not TICK:
		if isinstance(item, Query):
			state = grid.query(item.y, item.x)
			item = sim.send(state)
		else:
			progeny.assign(item.y, item.x, item.state)
			item = next(sim)
	return progeny




class ColumnPrinter(object):
	def __init__(self):
		self.columns = []

	def show(self):
		for c in self.columns:
			print(c)

grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
grid.assign(0, 4, ALIVE)
grid.assign(0, 2, ALIVE)
grid.assign(1, 3, ALIVE)


print(grid)

sim = simulate(grid.height, grid.width)
columns = ColumnPrinter()
for i in range(5):
	columns.columns.append(str(grid))
	grid = live_a_generation(grid, sim)

print(columns.show())
