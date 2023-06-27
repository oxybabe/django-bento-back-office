from django import forms

from .models import Appetizer, Dessert, MainCourse


class AppetizerForm(forms.ModelForm):
    class Meta:
        model = Appetizer
        fields = ['name', 'price', 'description']
        
        
class MainCourseForm(forms.ModelForm):
    class Meta:
        model = MainCourse
        fields = ['name', 'price', 'description']
        
class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ['name', 'price', 'description']