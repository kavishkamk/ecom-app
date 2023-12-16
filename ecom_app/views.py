from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category
from .models import User

from .forms import SignUpForm

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

def authentication(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            user.save()
            return HttpResponse("User Created")
    else:
        form = SignUpForm()

    return render(request, "ecom_app/authentication.html", {
        "form": form
    })
