from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nossa_equipe/", views.nossa_equipe, name="nossa_equipe"),
    path("tratamentos/", views.tratamentos, name="tratamentos"),
    path("tratamentos/estetica_corporal/", views.estetica_corporal, name="estetica_corporal"),
    path("tratamentos/limpeza_de_pele/", views.limpeza_de_pele, name="limpeza_de_pele"),
]

