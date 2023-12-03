from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("shop", views.category_preview, name="category-preview-page"),
    path("shop/<str:category_id>", views.catetory, name="categoy-page")
]