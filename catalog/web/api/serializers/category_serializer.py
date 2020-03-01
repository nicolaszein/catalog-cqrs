from catalog.web.api.serializers.base_serializer import BaseSerializer


class CategorySerializer(BaseSerializer):

    class Meta():
        fields = ('id', 'name', 'created_at', 'updated_at')
