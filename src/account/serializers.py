from rest_framework import serializers
from .models import User


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'birthday', 'name', 'surname', 'floor', 'language', 'family_status', 'social_status', 'place_of_living', 'children_have', 'pets']
