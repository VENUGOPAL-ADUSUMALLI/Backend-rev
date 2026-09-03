from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 20)
    price = models.IntegerField()
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.name} has price {self.price}"