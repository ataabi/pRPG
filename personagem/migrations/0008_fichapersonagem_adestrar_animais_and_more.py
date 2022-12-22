# Generated by Django 4.1.4 on 2022-12-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0007_fichapersonagem_acrobacia_delete_periciaspersonagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichapersonagem',
            name='adestrar_animais',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='arcanismo',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='atletismo',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='atuacao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='enganacao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='furtividade',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='historia',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='intimidacao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='intuicao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='investigação',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='medicina',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='natureza',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='percepcao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='persuasao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='prestidigitar',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='religiao',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='fichapersonagem',
            name='sobrevivencia',
            field=models.BooleanField(default='False'),
        ),
    ]