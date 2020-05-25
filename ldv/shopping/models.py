from django.db import models

# Create your models here.

class Clothes(models.Model):
    """
        Clothes table
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)

    def __str__(self):
        return self.name


class Meta:
    verbose_name = "Clothe"
    verbose_name_plural = "Clothes"