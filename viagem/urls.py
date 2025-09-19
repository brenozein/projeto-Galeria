from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('viagem/<int:id>/', views.viagem_detail, name='viagem_detail'),
    path('pesquisa/', views.pesquisar_viagens, name='pesquisar_viagens'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
