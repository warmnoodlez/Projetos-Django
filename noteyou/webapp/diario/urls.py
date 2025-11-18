from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('criaranotacao/', views.novodia, name='novodia'),
]