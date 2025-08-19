from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato', views.contato, name='contato'),
    path('wow', views.wow, name='wow'),
]