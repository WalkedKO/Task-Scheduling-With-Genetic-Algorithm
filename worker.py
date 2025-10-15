from dataclasses import dataclass
from product import Product
@dataclass()
class Worker:
    """
    Dataclass representing one worker.
    :param name: str
        worker's name
    :param can_produce: list(product)
        list of all products that the worker is able to produce
    """
    name: str
    can_produce: list