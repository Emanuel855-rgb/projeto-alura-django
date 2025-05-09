from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms, UploadForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
import uuid
# Create your views here.

def login(request):
    formulario_login = LoginForms()

    if request.method == "POST":
        login_dados = LoginForms(request.POST)
        
        if login_dados.is_valid():

            login_email = login_dados["email_login"].value()
            login_senha = login_dados["senha"].value()

            usuario = User.objects.filter(email = login_email).first()
            if usuario is not None and usuario.check_password(login_senha):
                auth.login(request, usuario)
                messages.success(request, "Login efetuado com sucesso!")
                return redirect("pag_app1")
            else:
                login_dados.add_error(None, "Usuário ou senha incorretos!")
                
        return render(request, 'usuarios/login.html', {"formulario": login_dados})
         
    return render(request, 'usuarios/login.html', {"formulario": formulario_login})


def cadastro(request):
    formulario_cadastro = CadastroForms()

    if request.method == "POST":
        formulario_dados = CadastroForms(request.POST)
        
        if formulario_dados.is_valid():
            
            formulario_nome = formulario_dados["nome_cadastro"].value()
            formulario_email = formulario_dados["email"].value()
            formulario_senha = formulario_dados["confirmar_senha"].value()
            primeiro_nome, sobrenome = formulario_dados.pegar_sobrenome()
           
            # Função para gerar nomes de usuarios
            def gerar_username(primeiro_nome, sobrenome):
                username_base = primeiro_nome.lower() + sobrenome.lower()
                username_unico = f"{username_base}_{uuid.uuid4().hex[:4]}"
                while User.objects.filter(username = username_unico).exists():
                    username_unico = f"{username_base}_{uuid.uuid4().hex[:4]}"
                return username_unico
            
            username_gerado = gerar_username(primeiro_nome, sobrenome)

            if User.objects.filter(email = formulario_email).exists():
                formulario_dados.add_error(None, "Email já cadastrado!")
                return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
            
            usuario = User.objects.create_user(
                username = username_gerado,
                email = formulario_email,
                password = formulario_senha,
                last_name = sobrenome.capitalize(),
                first_name = primeiro_nome.capitalize()
            )

            usuario.save()
            messages.success(request, f"{usuario.first_name} {usuario.last_name} cadastrado com sucesso!")
            return redirect("url_login")
        
        else:
            return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
        
    return render(request, 'usuarios/cadastro.html', {"formulario": formulario_cadastro})

def fazer_logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado!")
    return redirect("url_login")

def upload_imagem(request):
    if request.method == "POST":
        formulario = UploadForms(request.POST, request.FILES)
        if formulario.is_valid():
            fotografia = formulario.save(commit=False)
            fotografia.usuario = request.user
            fotografia.save()
            return redirect('pag_app1')
    else:
        formulario = UploadForms()

    return render(request, "usuarios/upload.html", {"formulario": formulario})