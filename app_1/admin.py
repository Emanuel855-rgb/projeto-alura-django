from django.contrib import admin
from app_1.models import Fotografia
# Register your models here.

class Lista(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "foto", "publicado")
    list_editable = ("publicado",)
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10
admin.site.register(Fotografia, Lista)