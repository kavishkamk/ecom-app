from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("shop", views.category_preview, name="category-preview-page"),
    path("shop/<slug:slug>", views.catetory, name="categoy-page"),
    path("authentication", views.authentication, name="authentication-page"),
]