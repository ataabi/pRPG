# Generated by Django 4.1.4 on 2022-12-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0003_fichapersonagem_dados_vida_fichapersonagem_pv_atual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichapersonagem',
            name='res_for',
            field=models.BooleanField(default='False'),
        ),
    ]
