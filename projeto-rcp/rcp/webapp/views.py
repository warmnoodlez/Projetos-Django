from django.shortcuts import render, get_object_or_404
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'index.html')

def telefones(request):
    return render(request, 'telefones.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def detalhe_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'dt-pessoa.html', {'pessoa': pessoa})