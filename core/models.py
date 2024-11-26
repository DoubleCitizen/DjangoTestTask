from django.db import models
from django.db.models import ForeignKey

from user.models import User


# Create your models here.
class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = ForeignKey(Car, on_delete=models.PROTECT)
    author = ForeignKey(User, on_delete=models.PROTECT)