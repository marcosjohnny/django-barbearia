from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import EnhancedLoginView, RegisterUserPage

# These are the URLs that will be used to access the views
urlpatterns = [
    # path('login/', EnhancedLoginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUserPage.as_view(), name='register'),
]