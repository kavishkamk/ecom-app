from django.shortcuts import render, get_object_or_404

from .models import Category

def index(request):

    categories = Category.objects.all()

    return render(request, "ecom_app/index.html", {
        "categories": categories
    })

def catetory(request, category_id):

    category = get_object_or_404(Category, route=category_id)
    
    return render(request, "ecom_app/category.html", {
        "category": category
    })

def category_preview(request):
    categories = Category.objects.all()

    return render(request, "ecom_app/category-preview.html", {
        "categories": categories
    })
