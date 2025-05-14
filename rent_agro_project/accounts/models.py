from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Арендодатель'),
        ('renter', 'Арендующий'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='renter')

    def is_owner(self):
        return self.role == 'owner'

    def is_renter(self):
        return self.role == 'renter'
