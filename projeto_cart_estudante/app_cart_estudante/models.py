from django.db import models

class Estudante(models.Model):
    id_estudante = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    dt_nascimento = models.DateField()
    email =models.EmailField()
    matricula = models.CharField(max_length=6, unique=True)
    periodo = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    telefone_emergencia = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    endereço = models.TextField()

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=6)
    password = models.TextField(max_length=255)
    email = models.EmailField()