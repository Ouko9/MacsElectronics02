from django import forms
from nicsapp.models import Products, ImageModel
from django.db import models

class MemberForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']


class CustomProductModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
