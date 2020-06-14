# Item 31a: Lookup Chain

"""
1. result returned from the __get__ method of the `data descriptor` named after the attribute you’re looking for.

2. If that fails, get the value of your object’s __dict__ for the key named after the attribute you’re looking for.

3. If that fails, get the result returned from the __get__ method of the `non-data descriptor` named after the attribute you’re looking for.

4. If that fails, get the value of your object type’s __dict__ for the key named after the attribute you’re looking for.

5. If that fails, get the value of your object parent type’s __dict__ for the key named after the attribute you’re looking for.

6. If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.

7. If everything else has failed, get an AttributeError exception
"""

class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")

print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_weels'])
print(type(my_car).__base__.__dict__['can_fly'])