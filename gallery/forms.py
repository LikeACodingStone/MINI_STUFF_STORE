from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Category

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['category', 'image', 'number'] 