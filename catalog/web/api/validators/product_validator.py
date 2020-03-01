from marshmallow import fields
from catalog.web.api.validators.base_validator import BaseValidator


class ProductValidator(BaseValidator):
    supplier_id = fields.UUID(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    color = fields.Str(required=True)
    weight = fields.Integer(required=True)
    price = fields.Float(required=True)
    categories = fields.List(fields.UUID())
