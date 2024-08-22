from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterUserPage

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUserPage.as_view(), name='register'),
]