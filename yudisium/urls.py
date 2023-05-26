from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tambah/', views.tambah),
    path('<int:id_yudisium>/update/', views.update),
    path('<int:id_yudisium>/hapus/', views.hapus),
]
