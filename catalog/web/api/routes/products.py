from flask import request, jsonify
from catalog.web.api import app

from catalog.web.api.validators.product_validator import ProductValidator
from catalog.web.api.serializers.product_serializer import ProductSerializer
from catalog.command.application.use_cases.create_product import (
    CreateProduct
)
from catalog.command.application.use_cases.commands.create_product_command \
    import CreateProductCommand


@app.route(f'/products', methods=['POST'])
def create_product():
    valid_data = ProductValidator().validate(data=request.json)
    command = CreateProductCommand(**valid_data)

    product = CreateProduct().execute(command)

    return jsonify(ProductSerializer().serialize(product)), 201
