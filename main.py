from worker import Worker
from product import Product
from individual import Schedule
A = Worker("A", [Product(0, "Alpha",[],2, 1), Product(1, "Beta", [], 5, 7)])
test = Schedule([A], [Product(0, "Alpha",[],2), Product(0, "Beta", [], 5)], 8)
test.randomize()
test.print()