## Item 9: Generator Expression for Large Comprehensions

'''
Generator expression does not materialize the whole output consequence when they are called. Instead, Generator Expressions
evaluate to an iterator that yeilds one item at a time.
'''

iterator = (len(x) for x in open('Speech.txt'))
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))