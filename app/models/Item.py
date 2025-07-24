from dataclasses import dataclass


@dataclass
class Item:
    article: str
    name: str
    price: float
