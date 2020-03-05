import datetime

from sqlalchemy import Table, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import mapper

from catalog.query.configs.database.database import Database
from catalog.query.domain.entities.product import Product

DATABASE = Database()
metadata = DATABASE.metadata

products = Table(
    'products',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('state', JSONB, nullable=False),
    Column(
        'created_at',
        DateTime(),
        nullable=False,
        default=datetime.datetime.utcnow
    ),
    Column(
        'updated_at',
        DateTime(),
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    ),
)

mapper(Product, products)
