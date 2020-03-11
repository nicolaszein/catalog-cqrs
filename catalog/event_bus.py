from async_bus import EventBus

from catalog.query.infra.repositories.products_repository import ProductsRepository

bus = EventBus()


@bus.subscribe('product_created')
async def create_query_product(state):
    ProductsRepository().create(state)
