from django.urls import path
from .views import HomeView, AddProductView

urlpatterns = [
    path("", HomeView, name="homepage"),
    path("adicionar/", AddProductView, name="add"),

]