# Generated by Django 5.1.2 on 2024-12-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart_estudante', '0002_auto_20241213_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=6)),
                ('password', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
