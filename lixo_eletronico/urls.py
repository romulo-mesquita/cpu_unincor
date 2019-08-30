from django.urls import path,include
from .import views


app_name = 'lixo_eletronico'

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos', views.eventos, name='eventos'),
    path('agenda_completa',views.agenda_completa, name='agenda_completa'),
    path('<int:eventos_id>', views.evento_detalhe, name='detalhe'),
    path('grupo_estudo', views.grupo, name='grupo_estudo'),
    path('contato', views.contato, name='contato'),
    path('success', views.success, name='success'),
]
