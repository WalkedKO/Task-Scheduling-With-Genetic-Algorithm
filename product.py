from dataclasses import dataclass
@dataclass()
class Product:
    """
    Dataclass representing a product
    :param name: str
        product's name
    :param needed: list(product)
        list of products (components) needed for producing this product
    :param time: int
        hours needed to produce the product
    :param value: int
        value of the finished product
    """
    name: str
    needed: list
    time: int
    value: int = 0
