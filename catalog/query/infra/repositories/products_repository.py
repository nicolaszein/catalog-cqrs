from catalog.query.configs.database import DATABASE

from catalog.query.domain.entities.product import Product


class ProductsRepository:

    def __init__(self):
        self.session = DATABASE.session

    def create(self, state):
        product = Product(id=state['id'], state=state)

        try:
            self.session.add(product)
            self.session.commit()
            self.session.flush()

            return product
        except Exception as e:
            self.session.rollback()

            raise e
