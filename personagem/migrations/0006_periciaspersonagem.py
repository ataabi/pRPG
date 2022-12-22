# Generated by Django 4.1.4 on 2022-12-16 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0005_alter_fichapersonagem_res_car_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PericiasPersonagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acrobacia', models.BooleanField(default='False')),
                ('ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personagem.fichapersonagem')),
            ],
        ),
    ]