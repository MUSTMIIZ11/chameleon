from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('download', views.update_img_url, name='img_url'),
    re_path(r'qrcode(.+)$', views.makeqrcode, name='qrcode'),
    path('download', views.download, name='download')
]