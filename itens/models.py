from django.db import models

# EQUIPAMENTO DE AVENTURA
class EquipamentoAventura(models.Model):
    MOEDAS = [('pc','Cobre'), ('pp','Prata'), ('pe','Electro'), ('po','Ouro'), ('pl','Platina')]
    nome = models.CharField(max_length=30)
    valor = models.IntegerField(default=0)
    moeda = models.CharField(max_length=2, choices=MOEDAS)
    peso = models.FloatField(default=0, null=True, blank=True)
    descricao = models.TextField(default='', null=True, blank=True)
    propriedades = models.TextField(default='', null=True, blank=True)
    habilidade = models.TextField(default='', null=True, blank=True)


