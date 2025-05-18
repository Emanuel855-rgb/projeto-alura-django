from django.urls import path
from apps.usuarios.views import login, cadastro, fazer_logout, upload_imagem, confirmar_email

urlpatterns = [
   path('login/', login, name='url_login'),
   path('cadastro/', cadastro, name='url_cadastro'),
   path('logout/', fazer_logout, name='url_logout'),
   path('upload/', upload_imagem, name='url_upload'),
   path('confirmar_email/', confirmar_email, name='url_confirmar_email')
]