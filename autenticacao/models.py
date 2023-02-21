from django.db import models
from django.utils.safestring import mark_safe

class Cargos(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    foto = models.ImageField(upload_to="foto")
    nome = models.CharField(max_length=100)
    sobrenomenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome

    def nome_completo(self):
        return f"{self.nome} {self.sobrenomenome}"

    @mark_safe
    def get_foto(self):
        return f'<img width="30px" src="/media/{self.foto}">'


class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
