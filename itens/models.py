from django.db import models

#Moedas do Personagem
# class MoedasPersonagem(models.Model):
#     personagem =  models.ForeignKey('BasePersonagem', on_delete=models.CASCADE)
#     pc = models.IntegerField(default=0)
#     pp = models.IntegerField(default=0)
#     pe = models.IntegerField(default=0)
#     po = models.IntegerField(default=0)
#     pl = models.IntegerField(default=0)

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


