from django.urls import path
from apps.app_1.views import index, imagem, buscar, categoria, minhas_fotos, categoria_minhas_fotos, imagem_minha_foto, excluir_imagem, editar_imagem

urlpatterns = [
    path('', index, name= 'pag_app1'),
    path('imagem/<int:foto_id>', imagem, name= 'imagem'),
    path("buscar/", buscar, name="buscar"),
    path("categoria/<str:buscar_categoria>", categoria, name="url_categoria"),
    path("minhas_fotos/", minhas_fotos, name="url_minhas_fotos"),
    path("categoria_minhass_fotos/<str:buscar_categoria>", categoria_minhas_fotos, name="url_categoria_minhas_fotos"),
    path("imagem_minha_foto/<int:foto_id>", imagem_minha_foto, name="url_imagem_minha_foto"),
    path("excluir_imagem/<int:foto_id>", excluir_imagem, name="url_excluir_imagem"),
    path("editar_imagem/<int:foto_id>", editar_imagem, name="url_editar_imagem")
]