from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:nim_mhs>/update/', views.update),
    path('<int:nim_mhs>/hapus/', views.hapus),
]
