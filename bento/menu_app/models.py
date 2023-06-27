
from django.db import models


# Create your models here.
class Appetizer(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)



    
    
    def __str__(self):
        return self.name

    
class MainCourse(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

    
class Dessert(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

    
    