# Generated by Django 4.1.4 on 2022-12-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0012_basepersonagem_ores_car_basepersonagem_ores_cons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_acrobacia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_adestrar_animais',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_arcanismo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_atletismo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_atuacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_enganacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_furtividade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_historia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_intimidacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_intuicao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_investigação',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_medicina',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_natureza',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_percepcao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_persuasao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_prestidigitar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_religiao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basepersonagem',
            name='ot_sobrevivencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='acrobacia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='adestrar_animais',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='arcanismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='atletismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='atuacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='enganacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='furtividade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='historia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='intimidacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='intuicao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='investigação',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='medicina',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='natureza',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='percepcao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='persuasao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='prestidigitar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='religiao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='res_car',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='res_cons',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='res_des',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='res_int',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='res_sab',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basepersonagem',
            name='sobrevivencia',
            field=models.BooleanField(default=False),
        ),
    ]