from enum import Enum
"""
Used for telling if the unit in schedule is start of producing or end
"""
class ProductTag(Enum):
    NORMAL = 0
    START = 1
    STOP = 2