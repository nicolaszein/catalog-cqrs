from dataclasses import dataclass


@dataclass
class CreateCategoryCommand:
    name: str

    def to_dict(self):
        return {
            'name': self.name
        }
