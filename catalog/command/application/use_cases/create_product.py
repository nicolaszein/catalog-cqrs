from catalog.command.application.use_cases.base_use_case import BaseUseCase
from catalog.exceptions import ObjectDoesNotExistError

from catalog.command.domain.entities.product import Product
from catalog.command.infra.repositories.products_repository import (
    ProductsRepository
)
from catalog.command.infra.repositories.suppliers_repository import (
    SuppliersRepository
)
from catalog.command.infra.repositories.categories_repository import (
    CategoriesRepository
)


class CreateProduct(BaseUseCase):

    def __init__(self):
        self.__products_repository = ProductsRepository()
        self.__suppliers_repository = SuppliersRepository()
        self.__categories_repository = CategoriesRepository()

    def execute(self, create_product_command):
        supplier_id = create_product_command.supplier_id
        supplier = self.__suppliers_repository.get(supplier_id)

        if not supplier:
            raise ObjectDoesNotExistError('Supplier')

        product = Product(**create_product_command.to_dict())
        product.supplier = supplier

        for category_id in create_product_command.categories:
            category = self.__categories_repository.get(category_id)
            if not category:
                raise ObjectDoesNotExistError('Category')

            product.categories.append(category)

        return self.__products_repository.create(product)
