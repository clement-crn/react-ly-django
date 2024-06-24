# In serializers.py
from rest_framework import serializers
from .models import Test

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'