from catalog.command.application.use_cases.base_use_case import BaseUseCase

from catalog.command.domain.entities.supplier import Supplier
from catalog.command.infra.repositories.suppliers_repository import (
    SuppliersRepository
)


class CreateSupplier(BaseUseCase):

    def __init__(self):
        self.__suppliers_repository = SuppliersRepository()

    def execute(self, create_supplier_command):
        supplier = Supplier(**create_supplier_command.to_dict())

        return self.__suppliers_repository.create(supplier)
