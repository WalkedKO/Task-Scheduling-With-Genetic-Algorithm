from worker import Worker
from product import Product
from individual import Schedule
A = Worker("A", [Product("Alpha",[],2, 1), Product("Beta", [], 5, 7)])
test = Schedule([A], [Product("Alpha",[],2), Product("Beta", [], 5)], 8)
test.randomize()
test.print()