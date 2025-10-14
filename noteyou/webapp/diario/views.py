from django.shortcuts import render

# Create your views here.

def diarioindex (request):
    return render(request, 'index.html')