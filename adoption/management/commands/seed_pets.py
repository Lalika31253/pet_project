#to run python manage.py seed_pets

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from adoption.models import Province, City, Branch, Pet, PetImage

import random

User = get_user_model()


CITY_DATA = {
    "AB": ["Edmonton", "Calgary", "Red Deer"],
    "BC": ["Vancouver", "Victoria", "Surrey"],
    "ON": ["Toronto", "Ottawa", "London"],
    "QC": ["Montreal", "Quebec City", "Laval"],
    "MB": ["Winnipeg", "Brandon"],
    "SK": ["Regina", "Saskatoon"],
    "NS": ["Halifax"],
    "NB": ["Fredericton", "Moncton"],
    "NL": ["St. John's"],
    "PE": ["Charlottetown"],
    "NT": ["Yellowknife"],
    "NU": ["Iqaluit"],
    "YT": ["Whitehorse"],
}


PET_NAMES = ["Max", "Luna", "Bella", "Charlie", "Rocky", "Milo", "Lucy", "Daisy"]
BREEDS = ["Labrador", "Husky", "Persian Cat", "Bulldog", "Beagle", "Golden Retriever"]


class Command(BaseCommand):
    help = "Seed full system: provinces, cities, branches, pets"

    def handle(self, *args, **kwargs):

        self.stdout.write("🌱 Seeding started...")

        # Create demo user (owner of pets)
        user, _ = User.objects.get_or_create(
            username="demo",
            defaults={"email": "demo@test.com"}
        )

        for code, cities in CITY_DATA.items():

            province, _ = Province.objects.get_or_create(code=code)

            for city_name in cities:

                city, _ = City.objects.get_or_create(
                    name=city_name,
                    province=province
                )

                branch, _ = Branch.objects.get_or_create(
                    name=city_name,
                    city=city,
                    address=f"{city_name} Center",
                    phone="000-000-0000"
                )

                # 🔥 CREATE PETS PER BRANCH
                for i in range(2):  # 2 pets per branch

                    pet = Pet.objects.create(
                        name=random.choice(PET_NAMES),
                        age=random.randint(1, 12),
                        breed=random.choice(BREEDS),
                        species=random.choice(["cat", "dog"]),
                        gender=random.choice(["male", "female"]),
                        description="Auto-generated test pet",
                        adoption_status="available",
                        pet_status="shelter",
                        branch=branch,
                        created_by=user,
                    )

        self.stdout.write(self.style.SUCCESS("✅ FULL SEED COMPLETE"))