from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


class Ngo(models.Model):
    ngo_name = models.CharField(max_length=200, null=True)
    # user = ngo name
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True)
    # owner_name = models.CharField(max_length=200, null=True)
    contact_number = models.FloatField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    # location details
    address = models.CharField(max_length=500, null=True)
    # usi api for states
    state = models.CharField(max_length=200, null=True)
    # logo
    logo = models.ImageField(null=True, blank=True, default='ngo.jpg')

    def __str__(self):
        return str(self.user)


class Donor(models.Model):
    name_user = models.CharField(max_length=200, null=True)
    # user is unique
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True)
    contact_number = models.FloatField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    # location details
    # address = models.CharField(max_length=500, null=True)
    # usi api for states
    # state = models.CharField(max_length=200, null=True)
    # logo
    # profile_pic = models.ImageField(null=True, blank=True, default='donor.png')

    def __str__(self):
        return str(self.user)
