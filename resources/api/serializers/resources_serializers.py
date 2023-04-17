from rest_framework import serializers
from resources.models import Resource


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        exclude = ('owner', 'state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'value': instance.value,
        }
