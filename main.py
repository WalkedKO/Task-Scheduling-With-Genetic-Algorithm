from setuptools.dist import check_specifier

from worker import Worker
from product import Product
from schedule import Schedule
from specie import Specie

# Usage example. Fast food restaurant.

# products:
potato = Product(5, "Raw fries", [], 5, 0)
fries = Product(0, "Fries",[potato], 5, 3)
meat = Product(6, "Hamburger raw meat", [], 10, 0)
hamburger = Product(1, "Hamburger", [meat], 5, 10)
cola = Product(2, "Cola", [], 1, 4)
meal = Product(3, "Full Meal", [cola, fries, hamburger], 2, 20)
coffe = Product(4, "Coffe", [], 2, 10)

# workers:
fryerA = Worker("Fryer A", [potato, fries, meat])
fryerB = Worker("Fryer B", [potato, fries, meat])
kitchen = Worker("Kitchen", [potato, hamburger])
cafe = Worker("Cafe", [cola, coffe])
service = Worker("Service", [meal, coffe, cola])
manager = Worker("Manager", [fries, meat, potato, hamburger, cola, meal, coffe])

#test = Schedule([fryerA, fryerB, kitchen, cafe, service, manager], [potato, fries, meat, hamburger, cola, meal, coffe], 10)
sp = Specie([fryerA, fryerB, kitchen, cafe, service, manager], [potato, fries, meat, hamburger, cola, meal, coffe], 60, 500, 100, 150)
best = sp.find_best()
#print the results
for i, result in enumerate(best):
    print("Best of ", i, " generation:")
    result.print()
print("BEST OF BEST IS: ")
max(best, key=lambda x: x[0]).print()