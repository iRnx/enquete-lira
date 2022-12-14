from django.db import models


class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=500)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.texto_pergunta


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=500)
    votar = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.texto_escolha