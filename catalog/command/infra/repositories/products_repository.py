from catalog.command.infra.repositories.base_repository import BaseRepository
from catalog.command.domain.entities.product import Product


class ProductsRepository(BaseRepository):
    _entity = Product
