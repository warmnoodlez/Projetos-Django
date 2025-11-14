from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from PIL import Image 

"""
Anotações:
---
Métodos GET e POST:
    - GET requisita dados que são armazenados no servidor, ou extrai os dados que são enviados através da URL.
      EX: https://exemplo.com/procura?termo=metodo+get onde '?' separa o endereço dos dados enviados, os dados são enviados em pares de variável e valor como 'termo=metodo+get'.

    - POST requista os dados de maneira oculta, não sendo visível na URL. Através desse método os dados também podem ser alterados.
      POST é recomendado em caso da 'extração' de dados sensíveis.
---
Para assuntos relacionados a sistema de autenticação, consultar: https://docs.djangoproject.com/pt-br/5.2/topics/auth/default/
---
"""

# Create your views here.
# Pega o modelo comum de um usuário e atribui na variável Usuario.
Usuario = get_user_model()

def home(request):
    return render(request, 'base.html')

def registro(request):
    # print(request.method)
    # if request.method == "POST":
    return render(request, 'usuarios/cadastro.html')

def entrar(request):
    return render(request, 'usuarios/entrar.html')


# Definindo função que realiza o cadastro de um usuário.
def cadastro_usuario(request):
    erro = None
    # Verifica se o método utilizado para compartilhamento de dados é POST, e atribui os dados à variáveis.
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        conf_senha = request.POST.get("conf_senha")
        foto = request.FILES.get("foto")

        # Verificações para que os campos obrigatórios sejam devidamente preenchidos.
        if not username or not email or not senha:
            erro = "Preencha os campos obrigatórios."
        elif senha != conf_senha:
            erro = "As senhas são diferentes."
        elif Usuario.objects.filter(username=username).exists():
            erro = "Esse nome de usuário já está sendo utilizado."
        else:
            # Se não houver empecilhos, o usuário será criado
            user = Usuario.objects.create_user(
                first_name = nome,
                last_name = sobrenome,
                username = username,
                email = email,
                password = make_password(senha),
            )
            
            # Se o usuário incluir uma foto, será incluído no perfil.
            if foto:
                user.foto = foto

            # Salvando o usuário.
            user.save()

        # Após a criação do perfil, redireciona o usuário à página do próprio perfil.        
            login(request, user)
            return redirect("perfil")

    return render(request, "usuarios/cadastro.html", {"erro": erro})
        

# Definindo função que realiza o login do usuário.

def login_usuario(request):
    erro = None

    # Verifica se o método de compartilhamento de dados é POST e atribui os dados às variáveis. 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verifica se os dados estão corretos.
        user = authenticate(request, username=username, password=password)

        # Se o usuário existir, é acessado a página do perfil dele; se não, é exibido um erro.
        if user is not None:
            login(request, user)
            return redirect("perfil")
        else:
            erro = "Nome de usuário ou senha incorretos."
            
        return render(request, "usuarios/entrar.html", {"erro":erro})
        

# Definindo função que realiza o logout do usuário e retorna à página de login.
def logout_usuario(request):
    logout(request)
    return redirect("entrar")

# Se o login for autenticado, executa e entra na página do perfil do usuário.
@login_required
def perfil(request):
    return render(request, "usuarios/perfil.html")