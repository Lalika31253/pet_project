from django import forms
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Pet, Branch, PetImage, City

User = get_user_model()


# ───────── PET FORM ─────────
class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = "__all__"


# ───────── PET IMAGE ─────────
class PetImageForm(forms.ModelForm):
    class Meta:
        model = PetImage
        fields = ["image"]


# ───────── USER FORM ─────────
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


# ───────── REGISTER FORM ─────────
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# ───────── LOST PET FORM ─────────
class LostPetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = [
            "name", "age", "breed", "species", "gender",
            "description",
            "pet_status", "adoption_status",
            "branch",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['pet_status'].choices = [
            ('lost', 'Lost'),
            ('found', 'Found'),
        ]


# ───────── BRANCH FORM ─────────
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ["name", "city", "address", "phone"]