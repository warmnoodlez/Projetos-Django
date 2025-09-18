from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('cadastrar/', views.cadastro_usuario, name="cadastrar")
]