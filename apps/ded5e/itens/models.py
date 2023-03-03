from django.db import models
from ded5e.personagem.models import BasePersonagem

# Items Comuns
class ItemsComuns(models.Model):
    MOEDAS = [('pc','Cobre'), ('pp','Prata'), ('pe','Electro'), ('po','Ouro'), ('pl','Platina')]
    nome = models.CharField(max_length=30)
    valor = models.IntegerField(default=0)
    moeda = models.CharField(max_length=2, choices=MOEDAS)
    peso = models.FloatField(default=0, null=True, blank=True)
    descricao = models.TextField(default='', null=True, blank=True)
    propriedades = models.TextField(default='', null=True, blank=True)
    habilidade = models.TextField(default='', null=True, blank=True)

# Base para as Armas e Armaduras
class ItemBase(models.Model):
    MOEDAS = [
        ('pc','Cobre'), ('pp','Prata'), 
        ('pe','Electro'), ('po','Ouro'), ('pl','Platina')
        ]

    personagem =  models.ForeignKey('personagem.BasePersonagem', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    preco = models.IntegerField(default=0)
    moeda = models.CharField(max_length=2, choices=MOEDAS)
    peso = models.FloatField(default=0, blank=True, null=True)
    descricao = models.TextField(default='', blank=True, null=True)
    fonte = models.CharField(max_length=128, blank=True, null=True, default='')


""" 
Armadura :
nome,Preco,CA,forca(pode ser none),Furtividade(bool),Peso,Descricao,
        (Categoria       - Vestir     - Remover
        Armadura Leve    - 1 minuto   - 1 minuto
        Armadura Média   - 5 minutos  - 1 minuto
        Armadura Pesada  - 10 minutos - 5 minutos
        Escudo           - 1 ação     - 1 ação)
"""
class Armaduras(ItemBase):
    CATEGORIAS = [('AL','Armadura Leve'),('AM','Armadura Média'),('AP','Armadura Pesada'),('E','Escudo')]
    ca = models.IntegerField(default=0)
    forca = models.IntegerField(default=0)
    furtividade = models.BooleanField()
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)

""" 
ARMAS
Nome, Preço, Dano, Peso, Propriedades,descrição

"""

class Armas(ItemBase):
    dano = models.CharField(max_length=30)
    propriedades = models.TextField(default='', blank=True)


class BolsaDeMoedas(models.Model):
    pc = models.IntegerField(default=0)
    pp = models.IntegerField(default=0)
    pe = models.IntegerField(default=0)
    po = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)