from catalog.command.infra.repositories.base_repository import BaseRepository
from catalog.command.domain.entities.product import Product
from catalog.event_bus import bus


class ProductsRepository(BaseRepository):
    _entity = Product

    def create(self, product):
        super().create(product)

        bus.emit('product_created', state=product.to_dict())

        return product
