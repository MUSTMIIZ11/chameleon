from django.urls import path

# from .views import CustomBackend
from . import views

urlpatterns = [
    path('', views.simple_login, name='login'),
    path('register/', views.signup, name='signup'),
]