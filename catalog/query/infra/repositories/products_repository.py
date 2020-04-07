from sqlalchemy.dialects.postgresql import array

from catalog.query.configs.database import DATABASE
from catalog.query.domain.entities.product import Product


class ProductsRepository:

    def __init__(self):
        self.session = DATABASE.session

    def create(self, state):
        category_ids = self.__build_category_ids(state)
        state['category_ids'] = category_ids
        product = Product(id=state['id'], state=state)

        try:
            self.session.add(product)
            self.session.commit()
            self.session.flush()

            return product
        except Exception as e:
            self.session.rollback()

            raise e

    def fetch_by_filters(self, **kwargs):
        query = self.session.query(Product)

        supplier = kwargs.get('supplier')
        category_ids = kwargs.get('category')

        if supplier:
            query = query.filter(Product.state['supplier']['id'].astext.in_([supplier]))

        if category_ids:
            category_ids = array(category_ids.split(','))

            query = query.filter(
                Product.state['category_ids'].op('?|')(category_ids)
            )

        return query.all()

    def __build_category_ids(self, state):
        return [category['id'] for category in state['categories']]
