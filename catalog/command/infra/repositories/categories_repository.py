from catalog.command.infra.repositories.base_repository import BaseRepository
from catalog.command.domain.entities.category import Category


class CategoriesRepository(BaseRepository):
    _entity = Category
