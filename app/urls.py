from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('jogo', views.jogo_view, name='jogo')
]
 # as demais rotas (listar, detalhes, criar, editar, excluir) entram aqui