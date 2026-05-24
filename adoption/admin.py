from django.contrib import admin
from .models import Pet, PetImage


class PetImageInline(admin.TabularInline):
    model = PetImage
    extra = 1


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [PetImageInline]