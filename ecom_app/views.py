from django.shortcuts import render

def index(request):
    return render(request, "ecom_app/index.html")

def catetory(request, category_id):
    return render(request, "ecom_app/category.html")

def category_preview(request):
    return render(request, "ecom_app/category-preview.html")
