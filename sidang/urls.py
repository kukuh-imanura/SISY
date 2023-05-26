from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:id_sidang>/update/', views.update),
    path('<int:id_sidang>/hapus/', views.hapus),
]
