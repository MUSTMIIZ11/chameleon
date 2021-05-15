from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save_map, name='save'),
    path('check', views.check, name='check'),
]