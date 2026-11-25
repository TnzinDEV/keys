<<<<<<< HEAD

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
urlpatterns = [
    path('', views.home_view, name='home'),
    path('jogo', views.jogo_view, name='jogo'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path( 'perfil/', views.perfil_view, name='perfil' ),
    path('jogo/<int:id>/' ,views.detalhes_jogo_view,name='detalhes'),
    path('cadastro/', views.cadastro_view, name='cadastro'),


]
=======

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
urlpatterns = [
    path('', views.home_view, name='home'),
    path('jogo', views.jogo_view, name='jogo'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path( 'perfil/', views.perfil_view, name='perfil' ),
    path('jogo/<int:id>/' ,views.detalhes_jogo_view,name='detalhes'),
    path('cadastro/', views.cadastro_view, name='cadastro'),


]
>>>>>>> b24fc8c7fd829fce604b98f2bb869ff40ed450cb
 # as demais rotas (listar, detalhes, criar, editar, excluir) entram aqui