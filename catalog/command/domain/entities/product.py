from catalog.command.domain.entities.base_entity import BaseEntity


class Product(BaseEntity):
    id = None
    supplier_id = None
    name = None
    description = None
    color = None
    weight = None
    price = None
    created_at = None
    updated_at = None

    supplier = None

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'supplier': self.__build_supplier(),
            'description': self.description,
            'color': self.color,
            'weight': self.weight,
            'price': self.price,
            'categories': self.__build_categories()
        }

    def __build_categories(self):
        return [dict(id=str(category.id), name=category.name) for category in self.categories]

    def __build_supplier(self):
        return dict(id=str(self.supplier.id), name=self.supplier.name)
