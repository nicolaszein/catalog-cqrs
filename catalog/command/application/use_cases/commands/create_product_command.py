import uuid
from dataclasses import dataclass, field


@dataclass
class CreateProductCommand:
    supplier_id: uuid.UUID
    name: str
    description: str
    color: str
    weight: int
    price: float
    categories: list = field(default_factory=list)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'color': self.color,
            'weight': self.weight,
            'price': self.price
        }
