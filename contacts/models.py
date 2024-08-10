from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    contact_picture = models.ImageField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
