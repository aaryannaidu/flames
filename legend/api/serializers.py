from rest_framework import serializers
from legend.models import FlamesResult

class FlamesResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlamesResult
        fields = ['id', 'name1', 'name2', 'result']

class FlamesCalculateSerializer(serializers.Serializer):
    name1 = serializers.CharField(max_length=100)
    name2 = serializers.CharField(max_length=100)
