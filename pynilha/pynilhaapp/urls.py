"""Routes of Pynilha."""
from django.urls import path
from . import views

urlpatterns = [

     path('', views.index, name='index'),

     path('mes/', views.mes, name='mes'),

     path('mes/<mes_a_detalhar>/',
          views.mes_detalhado,
          name='mes_detalhado'),

     path('mes/<mes_a_detalhar>/editar', views.editar, name='editar'),

     path('mes/<mes_a_detalhar>/confirmar_dados_receitas',
          views.confirmar_dados_receitas,
          name='confirmar_dados_receitas'),

     path('mes/<mes_a_detalhar>/confirmar_dados_despesas',
          views.confirmar_dados_despesas,
          name='confirmar_dados_despesas'),

     path('mes/<mes_a_detalhar>/confirmar_dados_aplicacoes',
          views.confirmar_dados_aplicacoes,
          name='confirmar_dados_aplicacoes'),
]
