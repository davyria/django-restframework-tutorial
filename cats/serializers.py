from rest_framework import serializers
from cats.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'description', 'birth_date', 'gender', 'breed', 'color')
