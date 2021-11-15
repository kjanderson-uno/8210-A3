from django.db import models
from django.urls import reverse


class Client(models.Model):
    customer_id = models.CharField(max_length=50, blank=True, default='00000')
    first_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    last_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    phone_number = models.CharField(max_length=50, default='(402)000-0000')
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    email = models.EmailField(max_length=100, default=' ')

    def __str__(self):
        return self.customer_id + ': ' + self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
