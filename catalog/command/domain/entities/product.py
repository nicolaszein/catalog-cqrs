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
