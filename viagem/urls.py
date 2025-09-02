from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('viagem/<int:id>/', views.viagem_detail, name='viagem_detail'),
    path('pesquisa/', views.pesquisar_viagens, name='pesquisar_viagens'),
]