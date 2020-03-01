from marshmallow import fields
from catalog.web.api.validators.base_validator import BaseValidator


class CategoryValidator(BaseValidator):
    name = fields.Str(required=True)
