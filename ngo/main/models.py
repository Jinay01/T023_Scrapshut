from django.db import models
from login.models import *

# Create your models here.


# class VerifiedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(ngo.is_verified=True)


class Requirements(models.Model):
    category = [
        ('medicine', 'medicine'),
        ('equipment', 'equipment'),
    ]

    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    # UPAR NU IGONORE KAR KHALE NICHE NA AA 3
    name = models.CharField(max_length=100)
    # category dropdown hase jema upar mentioned category select thase
    category = models.CharField(max_length=20, choices=category)

    # ketli quantity joie che
    initial_count = models.FloatField()
    donation_count = models.FloatField(default=0)

    # objects = models.Manager()
    # verified = VerifiedManager()
    # count = models.FloatField(default=0)

    # def get_pending(self):
    #     return self.initial_count - self.donation_count

    def __str__(self):
        return self.name


class Donate(models.Model):
    requirements_name = models.ForeignKey(
        Requirements, null=True, blank=True, on_delete=models.CASCADE)
    ngo = models.ForeignKey(
        Ngo, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        Donor, null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return str(self.requirements_name)
