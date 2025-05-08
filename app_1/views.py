from django.shortcuts import render, get_object_or_404
from app_1.models import Fotografia
# Create your views here.

def index(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, 'app_1/index.html', {"cards": fotografias, "opcoes_categoria": fotografia_categorias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'app_1/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_publicacao").filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    if "campo de busca" in request.GET:
        nome_busca = request.GET["campo de busca"]
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, "app_1/buscar.html", {"cards": fotografias, "opcoes_categoria": fotografia_categorias})

def categoria(request, buscar_categoria):
    fotos = Fotografia.objects.filter(categoria=buscar_categoria).filter(publicado=True)
    fotografia_categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, "app_1/categoria.html", {"cards": fotos, "opcoes_categoria": fotografia_categorias})