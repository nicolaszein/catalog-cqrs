from marshmallow import fields

from catalog.web.api.serializers.base_serializer import BaseSerializer


class ProductSerializer(BaseSerializer):
    categories = fields.Method("get_categories")

    class Meta():
        fields = (
            'id', 'name', 'description', 'color', 'weight', 'categories',
            'price', 'supplier_id', 'created_at', 'updated_at'
        )

    def get_categories(self, product):
        return [category.name for category in product.categories]
