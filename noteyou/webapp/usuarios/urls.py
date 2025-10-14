from django.urls import path
from . import views

urlpatterns = [ 
    # URL de páginas.
    path('registro/', views.registro, name='registro'), # Página com formulário de cadastro.
    path('', views.entrar, name='entrar'), # Página de Login.
    path('perfil/', views.perfil, name='perfil'), # Página de perfil.

    # URLs de funções.
    path('cadastrar/', views.cadastro_usuario, name="cadastrar"), # Função que cria o usuário.
    path('login/', views.login_usuario, name="login"), # Função que realiza o login
    path('logout/', views.logout_usuario, name="logout"), # Função que realiza o logout.
    
]