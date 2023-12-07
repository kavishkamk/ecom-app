from django.shortcuts import render, get_object_or_404

from .models import Category

def index(request):

    categories = Category.objects.all()

    return render(request, "ecom_app/index.html", {
        "categories": categories
    })

def catetory(request, slug):

    category = get_object_or_404(Category, slug=slug)
    category_items = category.items.all()
    
    return render(request, "ecom_app/category.html", {
        "category": category,
        "category_items": category_items
    })

def category_preview(request):
    categories = Category.objects.all()
    categories_preview = []

    for category in categories:
        categories_preview.append(
            {
                "category": category,
                "category_items": category.items.all()[:4]
            }
        )


    return render(request, "ecom_app/category-preview.html", {
        "categories_preview": categories_preview
    })
