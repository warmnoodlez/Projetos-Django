from django.shortcuts import render

# Create your views here.

def home (request):
    if request.user.is_authenticated:
        return render(request, 'pginicial/inicio.html')
    else:
        return render(request, 'pginicial/index.html')

# def verificacao (request):
#     if request.user.is_authenticated:
#         return render(request, '')
#     else:
#         redirect()