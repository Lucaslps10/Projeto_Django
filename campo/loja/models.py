from django.db import models

# Create your models here.

class Fornecedor(models.Model):

    nome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11)
    cidade = models.CharField(max_length = 70)
    bairro = models.CharField(max_length = 70)
    rua = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 15)
    data = models.DateField(default = None)

    def __str__(self):
        return self.nome

class Produto(models.Model):

    nome = models.CharField(max_length = 50)
    fabricante = models.CharField(max_length = 50)
    valor = models.IntegerField()
    data = models.DateField()
    estoque = models.IntegerField(max_length = 50)
    descricao = models.TextField(max_length = 200)

    def __str__(self):
        return self.nome