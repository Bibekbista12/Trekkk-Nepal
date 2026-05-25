from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('tourist', 'Tourist'),
        ('agency',  'Agency'),
    ]
    role        = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tourist')
    phone       = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    passport_no = models.CharField(max_length=50, blank=True)
    avatar      = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def is_agency(self):
        return self.role == 'agency'

    def __str__(self):
        return self.email