from django.contrib import admin

from .models import Category, CategoryItem
from .models import User

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class UserAdmin(admin.ModelAdmin):
    exclude = ["password"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem)
admin.site.register(User)