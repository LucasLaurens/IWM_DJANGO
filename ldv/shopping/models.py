from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
        Shopping User
    """


class Item(models.Model):
    """
     A inventory item
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="items")
    clothe = models.ForeignKey('Clothes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clothe.name} for {self.user.username}"


class Clothes(models.Model):
    """
        Clothes table
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)
    image = models.ImageField(null=True, default="/media/robe.jpg")

    def description_trunc(self):
        return self.description[:3]

    def __str__(self):
        return self.name


class Meta:
    verbose_name = "Clothe"
    verbose_name_plural = "Clothes"