from setuptools.dist import check_specifier

from worker import Worker
from product import Product
from individual import Schedule
from specie import Specie

# Usage example. Fast food restaurant.

# products:
potato = Product(5, "Raw fries", [], 1, 0)
fries = Product(0, "Fries",[potato], 2, 3)
meat = Product(6, "Hamburger raw meat", [], 2, 0)
hamburger = Product(1, "Hamburger", [meat], 2, 10)
cola = Product(2, "Cola", [], 1, 4)
meal = Product(3, "Full Meal", [cola, fries, hamburger], 1, 20)
coffe = Product(4, "Coffe", [], 2, 10)

# workers:
fryerA = Worker("Fryer A", [potato, fries, meat])
fryerB = Worker("Fryer B", [potato, fries, meat])
kitchen = Worker("Kitchen", [potato, hamburger])
cafe = Worker("Cafe", [cola, coffe])
service = Worker("Service", [meal, coffe, cola])
manager = Worker("Manager", [fries, meat, potato, hamburger, cola, meal, coffe])

test = Schedule([fryerA, fryerB, kitchen, cafe, service, manager], [potato, fries, meat, hamburger, cola, meal, coffe], 10)
sp = Specie([fryerA, fryerB, kitchen, cafe, service, manager], [potato, fries, meat, hamburger, cola, meal, coffe], 10, 100, 10, 80)
best = sp.find_best()
#print the results
for i in best:
    print("Best of ", i, " generation:")
    i.print()