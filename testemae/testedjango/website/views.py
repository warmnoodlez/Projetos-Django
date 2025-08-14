from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def wow(request):
    oxi="tu achou uma easter egg"
    return render(request, 'wow.html', {'oxi':oxi})