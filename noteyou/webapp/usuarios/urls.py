from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.entrar, name='entrar'),
    path('logout/', views.logout_usuario, name="sair"),
    path('perfil/', views.perfil, name='perfil'),
    path('cadastrar/', views.cadastro_usuario, name="cadastrar")
]