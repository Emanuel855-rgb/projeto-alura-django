from django.urls import path
from usuarios.views import login, cadastro, fazer_logout

urlpatterns = [
   path('login/', login, name='url_login'),
   path('cadastro/', cadastro, name='url_cadastro'),
   path('logout/', fazer_logout, name='url_logout')
]