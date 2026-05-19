from django import forms
from .models import Pet, User as CustomUser

# Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PetForm(forms.ModelForm):
    class Meta:
        model  = Pet
        fields = ['species', 'gender', 'pet_status', 'name', 'age',
                  'breed', 'description', 'image', 'location', 'adoption_status', 'branch']


class UserForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

class LostPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'age',
            'breed',
            'species',
            'gender',
            'description',
            'image',
            'location',
        ]