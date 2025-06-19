from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name = 'items', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name

    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='item_images', blank=True, null=True)
    # is_sold = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name