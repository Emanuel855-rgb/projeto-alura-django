from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms, UploadForms, CodigoConfirmacao
from django.contrib.auth.models import User
from django.contrib import auth, messages
import uuid
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
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
            if usuario is not None and usuario.check_password(login_senha):
                auth.login(request, usuario)
                messages.success(request, f"Logado como {usuario.username}")
                return redirect("pag_app1")
            else:
                login_dados.add_error(None, "Usuário ou senha incorretos!")
                
        return render(request, 'usuarios/login.html', {"formulario": login_dados})
         
    return render(request, 'usuarios/login.html', {"formulario": formulario_login})

def gerar_codigo():
    return str(random.randint(100000, 999999))

def enviar_confirmacao_email(destinatario_email, codigo_confirmacao):
    assunto = "Confirmação do seu Email"
    mensagem = f"Seu código de confirmação: {codigo_confirmacao}"
    send_mail(assunto, mensagem, settings.EMAIL_HOST_USER, 
              [destinatario_email], fail_silently=False)

def gerar_username(primeiro_nome, sobrenome):
    username_base = primeiro_nome.lower() + sobrenome.lower()
    username_unico = f"{username_base}_{uuid.uuid4().hex[:4]}"
    while User.objects.filter(username = username_unico).exists():
        username_unico = f"{username_base}_{uuid.uuid4().hex[:4]}"
    return username_unico

def cadastro(request):
    formulario_cadastro = CadastroForms()

    if request.method == "POST":
        formulario_dados = CadastroForms(request.POST)
        
        if formulario_dados.is_valid():
            formulario_nome = formulario_dados["nome_cadastro"].value()
            formulario_email = formulario_dados["email"].value()
            formulario_senha = formulario_dados["confirmar_senha"].value()
            primeiro_nome, sobrenome = formulario_dados.pegar_sobrenome()
            if User.objects.filter(email = formulario_email).exists():
                formulario_dados.add_error(None, "Email já cadastrado!")
                return render(request, "usuarios/cadastro.html", {"formulario": formulario_dados})
            
            username_gerado = gerar_username(primeiro_nome, sobrenome)

            usuario = User.objects.create_user(
                username= username_gerado,
                email= formulario_email,
                first_name = primeiro_nome,
                last_name = sobrenome,
                password= formulario_senha
            )
            usuario.is_active = False
            usuario.save()

            codigo_confirmacao = gerar_codigo()
        
            request.session["confirmar_email"] = {
                "codigo": codigo_confirmacao,
                "id_usuario": usuario.id
            }

            enviar_confirmacao_email(formulario_email, codigo_confirmacao)

            messages.success(request, "Enviamos um código para seu email")

            return redirect("url_confirmar_email")
        
        return render(request, 'usuarios/cadastro.html', {"formulario": formulario_dados})
    
    return render(request, 'usuarios/cadastro.html', {"formulario": formulario_cadastro})
    
def confirmar_email(request):
    formulario = CodigoConfirmacao()
    if request.method == "POST":
        formulario_codigo = CodigoConfirmacao(request.POST)
        codigo_inserido = request.POST.get("codigo_confirmacao")
        dados_confirmacao = request.session.get("confirmar_email")

        if not dados_confirmacao:
            messages.error(request, "Sessão expirada! ")
            return redirect("url_cadastro")

        if codigo_inserido == dados_confirmacao.get("codigo"):
            usuario = User.objects.get(id=dados_confirmacao.get("id_usuario"))
            usuario.is_active = True
            usuario.save()
            messages.success(request, "Conta cadastrada com sucesso!")
            del request.session["confirmar_email"]
            return redirect("url_login")
        
        else:
            messages.error(request, "Código incorreto!")
        
        return render(request, "usuarios/confirmar_email.html", {"formulario": formulario_codigo})
    return render(request, "usuarios/confirmar_email.html", {"formulario": formulario})

@login_required
def fazer_logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado!")
    return redirect("url_login")

@login_required
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