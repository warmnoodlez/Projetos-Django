from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('telefones/', views.telefones, name='telefones'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
]