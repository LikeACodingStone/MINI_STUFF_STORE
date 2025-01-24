from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField()  # 存储七牛云返回的URL
    number = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.number}" 