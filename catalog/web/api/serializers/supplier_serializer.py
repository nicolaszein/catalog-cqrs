from catalog.web.api.serializers.base_serializer import BaseSerializer


class SupplierSerializer(BaseSerializer):

    class Meta():
        fields = ('id', 'name', 'phone', 'created_at', 'updated_at')
