from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.URLField()

    def __str__(self):
        return f"{self.title} ({self.id})"
