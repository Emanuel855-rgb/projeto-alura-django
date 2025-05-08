from django.urls import path
from app_1.views import index, imagem, buscar, categoria

urlpatterns = [
    path('', index, name= 'pag_app1'),
    path('imagem/<int:foto_id>', imagem, name= 'imagem'),
    path("buscar/", buscar, name="buscar"),
    path("categoria/<str:buscar_categoria>", categoria, name="url_categoria")
]