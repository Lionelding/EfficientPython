# Item 22: Prefer Helper Classes
'''
	1. Avoid using dictionary within dictionary
	2. Use namedtuple with lightweight value before using a full class
'''

import collections

## `namedtuple`
Car = collections.namedtuple('Car', ('speed', 'position', 'color'))
myCar = Car(120, 55, 'red')

### iterable
for i in myCar:
	print(i)

### indexed
print(myCar[0])
print(myCar[1])
print(myCar[2])


## `Example 1` A three level system with namedtuple + class + dict
Grade = collections.namedtuple('Grade', ('score', 'weight'))

class Subject(object):
	def __init__(self):
		self._grades = []

	def report_grade(self, score, weight):
		self._grades.append(Grade(score, weight))

	def average_grade(self):
		total, total_weight = 0, 0
		for grade in self._grades:
			total = grade.score * grade.weight + total
			total_weight = grade.weight + total_weight
		return total / total_weight

class Student(object):
	def __init__(self):
		self._subjects = {}

	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()
		return self._subjects[name]

	def average_grade(self):
		total, count = 0, 0
		for subject in self._subjects.values():
			total = subject.average_grade() + total
			count = count + 1
		return total / count

class GradeBook(object):
	def __init__(self):
		self._students = {}

	def student(self, name):
		if name not in self._students:
			self._students[name] = Student()
		return self._students[name]

book = GradeBook()
albert = book.student('A E')
math = albert.subject('MATH')
math.report_grade(80, 0.1)
print(albert.average_grade())
