from django.db import models

# Create your models here.
class Nota(models.Model):
    nome_aluno = models.CharField(max_length = 200)
    disciplina = models.CharField(max_length = 200)
    nota_atividades =  models.CharField(max_length = 200)
    nota_trabalho = models.CharField(max_length = 200)
    nota_prova =  models.CharField(max_length = 200)
    media =  models.CharField(max_length = 200)
