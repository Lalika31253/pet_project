from rest_framework import serializers
from .models import Pet

#converts Django models into JSON
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'