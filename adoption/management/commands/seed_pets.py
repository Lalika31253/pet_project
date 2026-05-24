#to run python manage.py seed_pets

from django.core.management.base import BaseCommand
from adoption.models import Pet

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pet.objects.all().delete()

        pets = [
            ("Buddy", "available"),
            ("Luna", "pending"),
            ("Max", "adopted"),
            ("Kiwi", "available"),
        ]

        for name, status in pets:
            Pet.objects.create(
                name=name,
                age=2,
                breed="Test Breed",
                species="dog",
                gender="male",
                description="Seed pet",
                location="Edmonton",
                adoption_status=status,
                pet_status="shelter",
            )

        self.stdout.write(self.style.SUCCESS("Seed data created ✔"))