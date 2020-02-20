import datetime
import uuid

from sqlalchemy import (
    Table, Column, String, DateTime, Text, ForeignKey, Integer, Float,
    UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship

from catalog.command.configs.database.database import Database

from catalog.command.domain.entities.supplier import Supplier
from catalog.command.domain.entities.category import Category
from catalog.command.domain.entities.product import Product

DATABASE = Database()
metadata = DATABASE.metadata


suppliers = Table(
    'suppliers',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('name', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
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

mapper(Supplier, suppliers)

categories = Table(
    'categories',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('name', String(255), nullable=False),
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

mapper(Category, categories)

product_categories = Table(
    'product_categories',
    metadata,
    Column('product_id', UUID(as_uuid=True), ForeignKey('products.id')),
    Column('category_id', UUID(as_uuid=True), ForeignKey('categories.id')),
    UniqueConstraint(
        'product_id',
        'category_id',
        name='_unique_product_category'
    )
)

products = Table(
    'products',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('supplier_id', ForeignKey('suppliers.id'), nullable=False),
    Column('name', String(255), nullable=False),
    Column('description', Text(), nullable=True),
    Column('color', String(255), nullable=True),
    Column('weight', Integer(), nullable=False),
    Column('price', Float(), nullable=False),
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

mapper(Product, products, properties={
    'supplier': relationship(Supplier),
    'categories': relationship(Category, secondary=product_categories)
})
