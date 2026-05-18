from rest_framework import serializers
from .models import Pet, Branch, Favorite

#converts Django models into JSON

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    
    class Meta:
        model = Pet
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    pet = PetSerializer(read_only=True)
  
    class Meta:
        model = Favorite
        fields = '__all__'