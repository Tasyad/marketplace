from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=False, blank=False)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user}'