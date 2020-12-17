from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='images')
    description = models.TextField()


# only accessible from admin page
class ShopItem(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='images', null=True)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True)
