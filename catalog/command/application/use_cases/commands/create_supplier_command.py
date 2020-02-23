from dataclasses import dataclass


@dataclass
class CreateSupplierCommand:
    name: str
    phone: str

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone
        }
