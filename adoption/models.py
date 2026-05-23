from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Branch(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    opened_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.city})'


# class User(models.Model):
    
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username



class Pet(models.Model):

    CATEGORY_CHOICES = [
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        
    ]
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
    ]

    STATUS_CHOICES = [
        ('shelter', 'Shelter'),
        ('lost', 'Lost'),
        ('found', "Found")
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    species = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='pets/',
        blank=True,
        null=True
    )
    location = models.CharField(max_length=100)
    adoption_status = models.BooleanField(default=True)

    pet_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    branch = models.ForeignKey(
        'Branch',
        on_delete=models.CASCADE,
        related_name='pets',
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pets"
    )

    def __str__(self):
        return self.name



class AdoptionApplication(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} applied for {self.pet}'


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} likes {self.pet}"