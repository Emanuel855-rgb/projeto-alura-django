from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
import random
# Create your views here.

def login(request):
    formulario_login = LoginForms()

    if request.method == "POST":
        login_dados = LoginForms(request.POST)
        
        if login_dados.is_valid():

            login_email = login_dados["email_login"].value()
            login_senha = login_dados["senha"].value()

            usuario = User.objects.filter(email = login_email).first()
            print({usuario})
            if usuario is not None and usuario.check_password(login_senha):
                auth.login(request, usuario)
                return redirect("pag_app1")
            else:
                login_dados.add_error(None, "Usuário ou senha já existem!")
                
        return render(request, 'usuarios/login.html', {"formulario": login_dados})
         
    return render(request, 'usuarios/login.html', {"formulario": formulario_login})


def cadastro(request):
    formulario_cadastro = CadastroForms()

    if request.method == "POST":
        formulario_dados = CadastroForms(request.POST)
        
        if formulario_dados.is_valid():
            if formulario_dados["criar_senha"].value() != formulario_dados["confirmar_senha"].value():
                formulario_dados.add_error(None, "Por favor digite senhas iguais!")
                return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
            
            formulario_nome = formulario_dados["nome_cadastro"].value()
            formulario_email = formulario_dados["email"].value()
            formulario_senha = formulario_dados["criar_senha"].value()
            primeiro_nome, sobrenome = formulario_dados.pegar_sobrenome()
            formulario_username = primeiro_nome.lower() + sobrenome.lower() + str(random.randint(0, 100)) + str(random.randint(100, 1000)) + str(random.randint(1000, 100000))
            
            
            if User.objects.filter(email = formulario_email).exists() or User.objects.filter(username = formulario_username).exists():
                print("erro")
                formulario_dados.add_error(None, "Email ou usuário já exsitem!")
                return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
            
            usuario = User.objects.create_user(
                username = formulario_username,
                email = formulario_email,
                password = formulario_senha,
                last_name = sobrenome,
                first_name = primeiro_nome
            )

            usuario.save()
            return redirect("url_login")
        else:
            return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
        
    return render(request, 'usuarios/cadastro.html', {"formulario": formulario_cadastro})