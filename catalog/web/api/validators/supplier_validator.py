from marshmallow import fields, validate
from catalog.web.api.validators.base_validator import BaseValidator


class SupplierValidator(BaseValidator):
    name = fields.Str(required=True)
    phone = fields.Str(required=True, validate=validate.Length(max=20))
