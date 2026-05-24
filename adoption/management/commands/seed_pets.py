#to run python manage.py seed_pets


from django.core.management.base import BaseCommand
from adoption.models import Pet, Branch
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Seed database with sample branches and pets"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        Pet.objects.all().delete()
        Branch.objects.all().delete()

        user = User.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR("No user found! Create superuser first."))
            return

        # -----------------------------
        # 1. CREATE BRANCHES FIRST
        # -----------------------------
        branches = [
            Branch.objects.create(
                name="Edmonton Central",
                city="Edmonton",
                province="AB",
                address="Downtown Edmonton",
                phone="123456"
            ),
            Branch.objects.create(
                name="Calgary West",
                city="Calgary",
                province="AB",
                address="West Calgary",
                phone="123456"
            ),
            Branch.objects.create(
                name="Vancouver Branch",
                city="Vancouver",
                province="BC",
                address="Downtown Vancouver",
                phone="123456"
            ),
        ]

        # -----------------------------
        # 2. CREATE PETS
        # -----------------------------
        pets = [
            Pet(
                name="Buddy",
                age=3,
                breed="Golden Retriever",
                species="dog",
                gender="male",
                description="Friendly dog",
                pet_status="shelter",
                adoption_status="available",
                branch=branches[0],
                created_by=user,
            ),
            Pet(
                name="Mittens",
                age=2,
                breed="Tabby",
                species="cat",
                gender="female",
                description="Small cat",
                pet_status="shelter",
                adoption_status="available",
                branch=branches[1],
                created_by=user,
            ),
            Pet(
                name="Rocky",
                age=4,
                breed="Husky",
                species="dog",
                gender="male",
                description="Strong husky",
                pet_status="shelter",
                adoption_status="available",
                branch=branches[2],
                created_by=user,
            ),
        ]

        Pet.objects.bulk_create(pets)

        self.stdout.write(self.style.SUCCESS("Seeding completed!"))