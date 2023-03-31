from rest_framework import serializers
from .models import Drug

class DrugSerializer(serializers.Serializer):
    _key = serializers.CharField()
    description = serializers.ListField(child=serializers.CharField())

    # def create(self, validated_data):
    #     return Drug(**validated_data)
