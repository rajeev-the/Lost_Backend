# api/serializers.py

from rest_framework import serializers
from .models import ApiData

class ApiDataSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)  # Allow image uploads
    found = serializers.ReadOnlyField()
    class Meta:
        model = ApiData
        fields = '__all__'
