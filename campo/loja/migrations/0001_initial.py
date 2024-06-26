# Generated by Django 5.0.3 on 2024-03-22 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("cpf", models.CharField(max_length=11)),
                ("cidade", models.CharField(max_length=70)),
                ("bairro", models.CharField(max_length=70)),
                ("rua", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                ("data", models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("fabricante", models.CharField(max_length=50)),
                ("valor", models.IntegerField()),
                ("data", models.DateField()),
                ("estoque", models.IntegerField(max_length=50)),
                ("descricao", models.TextField(max_length=200)),
            ],
        ),
    ]
