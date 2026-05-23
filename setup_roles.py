import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pet_project.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from adoption.models import Pet, AdoptionApplication

# Create groups
admin_group, _ = Group.objects.get_or_create(name="Admin")
staff_group, _ = Group.objects.get_or_create(name="Shelter Staff")
user_group, _ = Group.objects.get_or_create(name="User")

# Permissions
pet_ct = ContentType.objects.get_for_model(Pet)
app_ct = ContentType.objects.get_for_model(AdoptionApplication)

pet_permissions = Permission.objects.filter(content_type=pet_ct)
app_permissions = Permission.objects.filter(content_type=app_ct)

# Assign permissions to staff
staff_group.permissions.set(list(pet_permissions) + list(app_permissions))

print("✅ Roles created successfully")