from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:nidn_petugas>/update/', views.update),
    path('<int:nidn_petugas>/hapus/', views.hapus),
]
