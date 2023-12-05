from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.URLField()
    route = models.CharField(max_length=100)

    def __str__(self):
        return f"title: {self.title}, id: {self.id}, route: {self.route}"
    
    def get_absolute_url(self):
        return reverse("categoy-page", args=[self.route])
    

class CategoryItem(models.Model):
    imageUrl = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, category: {self.category.title}"
