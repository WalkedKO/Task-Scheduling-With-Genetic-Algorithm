from worker import Worker
from product import Product
from individual import Schedule
alpha = Product(0, "Alpha",[],2, 1)
beta = Product(1, "Beta", [alpha], 5, 7)
A = Worker("A", [alpha, beta])
B = Worker("B", [alpha])
test = Schedule([A, B], [Product(0, "Alpha",[],2), Product(0, "Beta", [], 5)], 8)
test.randomize()
test.print()