# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()


# # ─────────────────────────────
# # PROVINCES (GLOBAL CONSTANT)
# # ─────────────────────────────
# PROVINCE_CHOICES = [
#     ("AB", "Alberta"),
#     ("BC", "British Columbia"),
#     ("ON", "Ontario"),
#     ("QC", "Quebec"),
#     ("MB", "Manitoba"),
#     ("SK", "Saskatchewan"),
#     ("NS", "Nova Scotia"),
#     ("NB", "New Brunswick"),
#     ("NL", "Newfoundland and Labrador"),
#     ("PE", "Prince Edward Island"),
#     ("NT", "Northwest Territories"),
#     ("NU", "Nunavut"),
#     ("YT", "Yukon"),
# ]

# class Province(models.Model):
#     code = models.CharField(max_length=2, choices=PROVINCE_CHOICES, unique=True)

#     def __str__(self):
#         return self.code

# # ─────────────────────────────
# # CITY MODEL
# # ─────────────────────────────
# class City(models.Model):
#     name = models.CharField(max_length=100)
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")

#     def __str__(self):
#         return f"{self.name} ({self.province})"

# # ─────────────────────────────
# # BRANCH MODEL
# # ─────────────────────────────
# class Branch(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} - {self.city}"

    

# # ─────────────────────────────
# # PET MODEL
# # ─────────────────────────────
# class Pet(models.Model):
#     CATEGORY_CHOICES = [
#         ("cat", "Cat"),
#         ("dog", "Dog"),
#     ]

#     GENDER_CHOICES = [
#         ("female", "Female"),
#         ("male", "Male"),
#     ]

#     STATUS_CHOICES = [
#         ("shelter", "Shelter"),
#         ("lost", "Lost"),
#         ("found", "Found"),
#     ]

#     ADOPTION_STATUS_CHOICES = [
#         ("available", "Available"),
#         ("pending", "Pending"),
#         ("adopted", "Adopted"),
#     ]

#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     breed = models.CharField(max_length=100)

#     species = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

#     description = models.TextField(blank=True)

#     adoption_status = models.CharField(
#         max_length=20,
#         choices=ADOPTION_STATUS_CHOICES,
#         default="available"
#     )

#     pet_status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default="shelter"
#     )

#     branch = models.ForeignKey(
#         Branch,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         # related_name="pets"
#     )

#     def __str__(self):
#         return self.name


# class PetImage(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="pets/")
    


# class AdoptionApplication(models.Model):

#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#     ]
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )
#     pet = models.ForeignKey(
#         Pet,
#         on_delete=models.CASCADE
#     )
#     message = models.TextField()
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='pending'
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user} applied for {self.pet}'


# class Favorite(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )
#     pet = models.ForeignKey(
#         Pet,
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return f"{self.user} likes {self.pet}"




from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# ─────────────────────────────
# PROVINCE CONSTANTS
# ─────────────────────────────
PROVINCE_CHOICES = [
    ("AB", "Alberta"),
    ("BC", "British Columbia"),
    ("ON", "Ontario"),
    ("QC", "Quebec"),
    ("MB", "Manitoba"),
    ("SK", "Saskatchewan"),
    ("NS", "Nova Scotia"),
    ("NB", "New Brunswick"),
    ("NL", "Newfoundland and Labrador"),
    ("PE", "Prince Edward Island"),
    ("NT", "Northwest Territories"),
    ("NU", "Nunavut"),
    ("YT", "Yukon"),
]


# ─────────────────────────────
# PROVINCE MODEL
# ─────────────────────────────
class Province(models.Model):
    code = models.CharField(max_length=2, choices=PROVINCE_CHOICES, unique=True)

    def __str__(self):
        return self.code


# ─────────────────────────────
# CITY MODEL
# ─────────────────────────────
class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    def __str__(self):
        return f"{self.name} ({self.province.code})"


# ─────────────────────────────
# BRANCH MODEL
# ─────────────────────────────
class Branch(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="branches"
    )

    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"


# ─────────────────────────────
# PET MODEL
# ─────────────────────────────
class Pet(models.Model):

    CATEGORY_CHOICES = [
        ("cat", "Cat"),
        ("dog", "Dog"),
    ]

    GENDER_CHOICES = [
        ("female", "Female"),
        ("male", "Male"),
    ]

    STATUS_CHOICES = [
        ("shelter", "Shelter"),
        ("lost", "Lost"),
        ("found", "Found"),
    ]

    ADOPTION_STATUS_CHOICES = [
        ("available", "Available"),
        ("pending", "Pending"),
        ("adopted", "Adopted"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)

    species = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    description = models.TextField(blank=True)

    adoption_status = models.CharField(
        max_length=20,
        choices=ADOPTION_STATUS_CHOICES,
        default="available"
    )

    pet_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="shelter"
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pets"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pets",
        null=True,
        blank=True)


    def __str__(self):
        return self.name


# ─────────────────────────────
# PET IMAGES
# ─────────────────────────────
class PetImage(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="pets/")

    def __str__(self):
        return f"{self.pet.name} image"


# ─────────────────────────────
# ADOPTION APPLICATION
# ─────────────────────────────
class AdoptionApplication(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.pet}"


# ─────────────────────────────
# FAVORITES
# ─────────────────────────────
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.pet}"