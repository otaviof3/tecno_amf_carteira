# Generated by Django 5.1.2 on 2024-12-13 15:01

from django.db import migrations

def create_estudante(apps, schema_editor):
    Estudante = apps.get_model('app_cart_estudante', 'Estudante')

    Estudante.objects.create(
        nome="Otávio Ferreira Dahlke",
        dt_nascimento="2004-06-03",
        email="otaviofd03@gmail.com",
        matricula="007053",
        periodo="5°",
        telefone="55997171476",
        telefone_emergencia="55996030702",
        cidade="Restinga Seca, RS",
        endereço="Rua Santos Dumont, 1391, Centro"
    )

class Migration(migrations.Migration):

    dependencies = [
        ('app_cart_estudante', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_estudante),
    ]
