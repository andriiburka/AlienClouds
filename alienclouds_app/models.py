from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='images', default='logo.png', blank=True)
    description = models.TextField(blank=True)


# only accessible from admin page
class ShopItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='images', default='logo.png')
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True)
