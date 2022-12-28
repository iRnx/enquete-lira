from django.db import models


class Sub_Categoria(models.Model):
    nome_sub_categoria = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome_sub_categoria


class Categoria(models.Model):
    nome_categoria  = models.CharField(max_length=200)
    sub_categoria = models.ManyToManyField(Sub_Categoria)

    def __str__(self) -> str:
        return self.nome_categoria


class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.texto_pergunta


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=500)
    votar = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.texto_escolha