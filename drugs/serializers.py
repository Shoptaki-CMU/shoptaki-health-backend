from rest_framework import serializers
from .models import Drug

class DrugSerializer(serializers.Serializer):
    _key = serializers.CharField()
    description = serializers.ListField(child=serializers.CharField())
    adverse_reactions_table = serializers.ListField(child=serializers.CharField())
    dosage_and_administration_table = serializers.ListField(child=serializers.CharField())
    drug_interactions_table = serializers.ListField(child=serializers.CharField())
    warnings_and_cautions_table = serializers.ListField(child=serializers.CharField())
    precautions_table = serializers.ListField(child=serializers.CharField())

