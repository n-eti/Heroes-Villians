from rest_framework import serializers
from .models import SuperType

class Super_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type', 'id']