# Generated by Django 4.1.4 on 2022-12-20 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0013_basepersonagem_ot_acrobacia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepersonagem',
            name='tendencia',
            field=models.CharField(choices=[('LB', 'Leal e Bom'), ('NB', 'Neutro e Bom')], max_length=20),
        ),
    ]
