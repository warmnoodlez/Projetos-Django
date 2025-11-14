from django.shortcuts import render

# Create your views here.

def journal(request):
    return render(request, 'diario/index.html')