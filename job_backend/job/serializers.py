from rest_framework import serializers

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = [
            'id',
            'title',
        ]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'position_salary',
            'position_location',
            'company_name',
            'created_at_formatted'
        ]

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'position_salary',
            'position_location',
            'company_name',
            'company_location',
            'company_email',
            'created_at_formatted',
        ]

