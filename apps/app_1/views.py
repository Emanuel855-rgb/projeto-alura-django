from django.shortcuts import render, get_object_or_404, redirect
from apps.app_1.models import Fotografia
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.usuarios.forms import UploadForms
# Create your views here.

def index(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, 'app_1/index.html', {"cards": fotografias, "opcoes_categoria": fotografia_categorias})

@login_required
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'app_1/imagem.html', {"fotografia": fotografia})

@login_required
def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    if "campo de busca" in request.GET:
        nome_busca = request.GET["campo de busca"]
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, "app_1/buscar.html", {"cards": fotografias, "opcoes_categoria": fotografia_categorias})

@login_required
def categoria(request, buscar_categoria):
    fotos = Fotografia.objects.filter(categoria=buscar_categoria).filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, "app_1/categoria.html", {"cards": fotos, "opcoes_categoria": fotografia_categorias})

@login_required
def minhas_fotos(request):
    usuario_fotos = request.user
    fotos = Fotografia.objects.filter(usuario=usuario_fotos).order_by("-data_publicacao")
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, "app_1/minhas_fotos.html", {"cards": fotos, "opcoes_categoria": fotografia_categorias})

@login_required
def categoria_minhas_fotos(request, buscar_categoria):
    usuario_fotos = request.user
    fotos = Fotografia.objects.filter(usuario=usuario_fotos, categoria = buscar_categoria)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, "app_1/categorias_minhas_fotos.html", {"cards": fotos, "opcoes_categoria": fotografia_categorias})

@login_required
def imagem_minha_foto(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "app_1/imagem_minha_foto.html", {"fotografia": fotografia})

@login_required
def excluir_imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    if request.user == foto.usuario:
        foto.delete()
        messages.success(request, "Fotografia deletada com sucesso!")
        return redirect("url_minhas_fotos")
    
@login_required
def editar_imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    form = UploadForms(instance=fotografia)

    if request.method == "POST":
        form = UploadForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto editada com sucesso!")
            return redirect("url_minhas_fotos")
        
    return render(request, "app_1/editar_foto.html", {"formulario":form, "foto_id": foto_id} )