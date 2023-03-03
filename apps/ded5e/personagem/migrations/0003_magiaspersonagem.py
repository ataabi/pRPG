# Generated by Django 4.1.4 on 2023-02-09 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personagem", "0002_inventariopersonagem_item_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="MagiasPersonagem",
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
                ("nome", models.CharField(max_length=100)),
                ("nivel", models.IntegerField()),
                ("tempo_conjuracao", models.CharField(max_length=50)),
                ("alcance", models.CharField(max_length=50)),
                ("componentes", models.CharField(max_length=100)),
                ("duraçao", models.CharField(max_length=25)),
                ("descricao", models.TextField()),
                (
                    "personagem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="personagem.basepersonagem",
                    ),
                ),
            ],
        ),
    ]