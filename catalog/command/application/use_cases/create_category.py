from catalog.command.application.use_cases.base_use_case import BaseUseCase

from catalog.command.domain.entities.category import Category
from catalog.command.infra.repositories.categories_repository import (
    CategoriesRepository
)


class CreateCategory(BaseUseCase):

    def __init__(self):
        self.__categories_repository = CategoriesRepository()

    def execute(self, create_category_command):
        category = Category(**create_category_command.to_dict())

        return self.__categories_repository.create(category)
