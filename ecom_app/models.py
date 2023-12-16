from collections.abc import Iterable
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.URLField()
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)

    def __str__(self):
        return f"title: {self.title}, id: {self.id}, slug: {self.slug}"
    
    def get_absolute_url(self):
        return reverse("categoy-page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class CategoryItem(models.Model):
    imageUrl = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, category: {self.category.title}"
    
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"username: {self.username}, email: {self.email}, id: {self.id}"
