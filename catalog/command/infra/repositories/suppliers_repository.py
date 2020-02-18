from catalog.command.infra.repositories.base_repository import BaseRepository
from catalog.command.domain.entities.supplier import Supplier


class SuppliersRepository(BaseRepository):
    _entity = Supplier
