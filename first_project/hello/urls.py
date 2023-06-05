#Importar una  biblioteca administradora de rutas
# admin de rutas
from django.urls import path
#importando listas
from .import views
# declarando las rutas validas
urlpatterns=[
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
]