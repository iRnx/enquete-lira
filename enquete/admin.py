from django.contrib import admin
from .models import Pergunta, Resposta, Categoria, Sub_Categoria



@admin.register(Sub_Categoria)
class Sub_CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_sub_categoria',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria',)


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pergunta', 'sub_categoria', 'data_publicacao')


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'resposta_pergunta', 'votar')
