# Generated by Django 4.1.4 on 2023-01-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariopersonagem',
            name='item_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]