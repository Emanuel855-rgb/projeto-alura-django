from django.contrib import admin
from apps.app_1.models import Fotografia
# Register your models here.

class Lista(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "foto", "publicado")
    list_editable = ("publicado",)
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuario",)
    list_per_page = 10
    exclude = ('usuario',)
    def save_model(self, request, obj, form, change):
        if not change:    
            obj.usuario = request.user  
        super().save_model(request, obj, form, change)
admin.site.register(Fotografia, Lista)