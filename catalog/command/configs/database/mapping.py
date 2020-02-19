import datetime
import uuid

from sqlalchemy import Table, Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper

from catalog.command.configs.database.database import Database

from catalog.command.domain.entities.supplier import Supplier

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
