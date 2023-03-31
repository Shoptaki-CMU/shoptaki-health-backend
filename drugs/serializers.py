from rest_framework import serializers
from .models import Drug

class DrugSerializer(serializers.Serializer):
    _key = serializers.CharField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    def create(self, validated_data):
        return Drug(**validated_data)
