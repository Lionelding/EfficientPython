# Item 9: Generator Expression for Large Comprehensions

'''
Generator expression does not materialize the whole output consequence when they are called. Instead, Generator Expressions
evaluate to an iterator that yeilds one item at a time.
Advantages:
	1. Memory Efficient
	2. Can be compounded together
Watch-out:
	1. Stateful. Not to use them more than once.
'''

## With List Comprehensions

results_list = [len(x) for x in open('Speech.txt')]
print(results_list)

## With Generator Expression. 

iterator = (len(x) for x in open('Speech.txt'))
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))

fancy_iterator = ((x, x**2) for x in iterator)
print(fancy_iterator)

print(next(fancy_iterator))
print(next(fancy_iterator))
print(next(fancy_iterator))
