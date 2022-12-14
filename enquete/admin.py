from django.contrib import admin
from .models import Pergunta, Resposta

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pergunta', 'data_publicacao')
    


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'texto_escolha', 'votar')
