# item 0: What is a Generator
'''
1. Contains `yield`
2. when called, return an iterator
3. Once yeilds, the function is paused and control is transferred to the caller. Local variables are remembered between successive calls
Advantages:
	1. Easy to implement
	2. Memory efficient
	3. Represent Infinite Stream with Finite lines
	4. Compounded Generator

'''

def my_generator():
	n = 1
	print('YI')
	yield n 
	n = n + 1

	print('ER')
	yield n
	n = n + 1

	print('SAN')
	yield n
	n = n + 1

## Local variables are kept between calls
## Manually
res = my_generator()
print(next(res))
print(next(res))
print(next(res))

## For loop
for i in my_generator():
	print(i)

## A more realistic usecase
def reverse_str(mystr):
	total = len(mystr)
	for i in range(total-1, -1, -1):
		yield mystr[i]

for char in reverse_str("Hello"):
	print(char)


## `Advantage 1`: Easy to implement
def PowTwoGen(max=0):
	n = 0
	while n < max:
		yield n**2
		n = 1 + n

a = PowTwoGen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

## `Advantage 3`: Represent Infinite Stream with Finite lines
def all_even():
	n = 0
	while True:
		yield n*2 
		n = 1 + n

b = all_even()
print(next(b))  
print(next(b))  
print(next(b))  
print(next(b))  

## `Advantage 4`: Compounded Generator
def fibonacci_numbers(nums):
	x, y = 0, 1
	for _ in range(nums):
		x, y = y, x+y
		yield x

def square(nums):
	for num in nums:
		yield num**2

print(list(square(fibonacci_numbers(5))))


