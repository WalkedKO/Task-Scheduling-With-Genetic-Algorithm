from dataclasses import dataclass
from productTag import ProductTag
@dataclass()
class Product:
    """
    Dataclass representing a product
    :param id: int
        Id number
    :param name: str
        product's name
    :param needed: list(product)
        list of products (components) needed for producing this product
    :param time: int
        time units needed to produce the product
    :param value: int
        value of the finished product
    :param tag: ProductTag
        used for telling if the unit in schedule is start of producing or end
    """
    id: int
    name: str
    needed: list
    time: int
    value: int = 0
    tag: ProductTag = ProductTag.NORMAL
