from django.shortcuts import render

# Create your views here.

def home (request):
    if request.user.is_authenticated:
        return render(request, 'inicio.html')
    else:
        return render(request, 'index.html')

# def verificacao (request):
#     if request.user.is_authenticated:
#         return render(request, '')
#     else:
#         redirect()