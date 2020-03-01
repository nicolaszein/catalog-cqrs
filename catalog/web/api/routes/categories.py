from flask import request, jsonify
from catalog.web.api import app

from catalog.web.api.validators.category_validator import CategoryValidator
from catalog.web.api.serializers.category_serializer import CategorySerializer
from catalog.command.application.use_cases.create_category import (
    CreateCategory
)
from catalog.command.application.use_cases.commands.create_category_command \
    import CreateCategoryCommand


@app.route(f'/categories', methods=['POST'])
def create_category():
    valid_data = CategoryValidator().validate(data=request.json)
    command = CreateCategoryCommand(**valid_data)

    category = CreateCategory().execute(command)

    return jsonify(CategorySerializer().serialize(category)), 201
