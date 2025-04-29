from django.urls import path
from usuarios.views import login, cadastro

urlpatterns = [
   path('login/', login, name='url_login'),
   path('cadastro/', cadastro, name='url_cadastro')
]