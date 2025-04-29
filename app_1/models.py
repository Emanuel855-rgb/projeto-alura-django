from django.db import models
from datetime import datetime
# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSO", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]       

    nome = models.CharField(max_length=100, null=False, blank=False) # "null= False" não pode ser um campo vazio, "blank = False" não pode ser algo irrelevante ex: " ".
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicado = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return self.nome