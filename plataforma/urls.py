from argparse import Namespace
from cgitb import html
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imovel/<str:id>', views.imovel, name="imovel"),
    path('agendar_visitas', views.agendar_visitas, name="agendar_visitas"),
    path('agendamentos', views.agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name="cancelar_agendamento"),
]
