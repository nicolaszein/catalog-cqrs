from flask import request, jsonify
from catalog.web.api import app

from catalog.web.api.validators.supplier_validator import SupplierValidator
from catalog.web.api.serializers.supplier_serializer import SupplierSerializer
from catalog.command.application.use_cases.create_supplier import (
    CreateSupplier
)
from catalog.command.application.use_cases.commands.create_supplier_command \
    import CreateSupplierCommand


@app.route(f'/suppliers', methods=['POST'])
def create_supplier():
    valid_data = SupplierValidator().validate(data=request.json)
    command = CreateSupplierCommand(**valid_data)

    supplier = CreateSupplier().execute(command)

    return jsonify(SupplierSerializer().serialize(supplier)), 201
