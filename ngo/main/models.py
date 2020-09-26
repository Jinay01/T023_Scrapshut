from django.db import models
from login.models import Ngo

# Create your models here.


class requirements(models.Model):
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
    count = models.IntegerField()
