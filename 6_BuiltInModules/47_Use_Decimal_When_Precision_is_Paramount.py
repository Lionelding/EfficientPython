# Item 47: Use `Decimal` When Precision is Paramount
"""
1. The `Decimal` class is ideal for situations that require high precision and exact rounding behavior
"""

import decimal
from decimal import Decimal


print("######### Example 1 #########")
## Example 1: Numbers are too small to round
rate = 1.45
seconds = 3*60 + 42
cost = rate*seconds/60
print(cost)
print(round(cost, 2))

rate = 0.05
seconds = 5
cost = rate * seconds / 60
print(cost)
print(round(cost, 2))

print("######### Example 2 #########")
## Example 2: Use `Decimal` class
rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)
print(rounded)

rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
print(cost)
rounded = cost.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)
print(rounded)


