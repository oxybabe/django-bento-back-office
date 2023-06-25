from django.contrib import admin
from .models import Appetizer, MainCourse, Dessert

admin.register(Appetizer, MainCourse, Dessert)(admin.ModelAdmin)

# Register your models here.
