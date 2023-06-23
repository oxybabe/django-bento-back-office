from django.db import models


# Create your models here.
class Appetizer(models.Model):
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10)
    description = models.CharField(max_length=100)

    
    
    def __str__(self):
        return self.name

    
class MainCourse(models.Model):
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Dessert(models.Model):
    name = models.CharField(max_length=100)
    japanese_name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    