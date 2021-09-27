from django.db import models
from django.urls import reverse


class Vehicle(models.Model):
    VIN = models.CharField(max_length=50, blank=False, null=False, default=' ')
    status = models.CharField(max_length=50, blank=False, null=False, default=' ')
    price = models.CharField(max_length=50, blank=False, null=False, default=' ')
    condition = models.CharField(max_length=50, blank=False, null=False, default=' ')
    picture = models.CharField(max_length=50, blank=False, null=False, default=' ')
    year_manufactured = models.CharField(max_length=50, blank=False, null=False, default=' ')
    make = models.CharField(max_length=50, blank=False, null=False, default=' ')
    model = models.CharField(max_length=50, blank=False, null=False, default=' ')
    trim = models.CharField(max_length=50, blank=False, null=False, default=' ')
    body_style = models.CharField(max_length=50, blank=False, null=False, default=' ')
    mileage = models.CharField(max_length=50, blank=False, null=False, default=' ')
    fuel_type = models.CharField(max_length=50, blank=False, null=False, default=' ')
    mpg = models.CharField(max_length=50, blank=False, null=False, default=' ')
    interior_color = models.CharField(max_length=50, blank=False, null=False, default=' ')
    exterior_color = models.CharField(max_length=50, blank=False, null=False, default=' ')

    def __str__(self):
        return self.exterior_color + ' ' + self.year_manufactured + ' ' + self.make + ' ' + self.model + ' ' + self.trim

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])
