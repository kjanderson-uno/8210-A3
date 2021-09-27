from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, default=' ', null=True, blank=True)
    last_name = models.CharField(max_length=50, default=' ', null=True, blank=True)
    hire_date = models.DateTimeField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, default=' ', null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, default=' ', null=True, blank=True)
    state = models.CharField(max_length=50, default=' ', null=True, blank=True)
