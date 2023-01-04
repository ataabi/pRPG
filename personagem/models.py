from django.db import models

# Create your models here.

class BasePersonagem(models.Model):
    # Informações Basicas
    nome_jogador = models.CharField(max_length=30)
    nome_personagem = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    classe = models.CharField(max_length=30)
    arquetipo = models.CharField(max_length=30,default='')
    nivel = models.IntegerField(default=1)
    antecedente = models.CharField(max_length=15)
    tendencia = models.CharField(max_length=20)
    divindade = models.CharField(max_length=30, default='')
    terra_natal = models.CharField(max_length=30, default='')
    iniciativa = models.IntegerField(default=0)
    c_a = models.IntegerField(default=0)
    deslocamento = models.IntegerField(default=0)
    inspiracao = models.IntegerField(default=0)
    proficiencia = models.IntegerField(default=0)
    pv_maximo = models.IntegerField(default=0)
    pv_atual = models.IntegerField(default=0)
    dados_vida = models.IntegerField(default=0)
    idiomas = models.CharField(max_length=120, default='Comum')

    def __str__(self):
        return self.nome_personagem

    # Habilidades
    forca = models.IntegerField(default=1, null=True)
    destreza = models.IntegerField(default=1, null=True)
    constituicao = models.IntegerField(default=1, null=True)
    inteligencia = models.IntegerField(default=1, null=True)
    sabedoria = models.IntegerField(default=1, null=True)
    carisma = models.IntegerField(default=1, null=True)
    

    # Modificadores de Habilidade
    @property
    def mod_forca(self):
        return int((self.forca-10)/2)
    @property
    def mod_destreza(self):
        return int((self.destreza-10)/2)
    @property
    def mod_constituicao(self):
        return int((self.constituicao-10)/2)
    @property
    def mod_inteligencia(self):
        return int((self.inteligencia-10)/2)
    @property
    def mod_sabedoria(self):
        return int((self.sabedoria-10)/2)
    @property
    def mod_carisma(self):
        return int((self.carisma-10)/2)
    #Fim dos modificadores

    @property
    def sabedoria_passiva(self):
        return int(10+self.mod_sabedoria)

    @property
    def limite_carga(self):
        return int(7.5*self.forca)

    #Testes de Resistencia
    
    # FORCA
    res_for = models.BooleanField(default=False, null=True)
    ores_for = models.IntegerField(default=0, null=True)
    @property
    def valor_res_for(self):
        if self.res_for:
            return self.mod_forca + self.proficiencia + self.ores_for
        else:
            return self.mod_forca + self.ores_for

    # DESTREZA
    res_des = models.BooleanField(default=False, null=True)
    ores_des = models.IntegerField(default=0, null=True)
    @property
    def valor_res_des(self):
        if self.res_des:
            return self.mod_destreza + self.proficiencia + self.ores_des
        else:
            return self.mod_destreza + self.ores_des

    # CONSTITUIÇÂO
    res_cons = models.BooleanField(default=False, null=True)
    ores_cons = models.IntegerField(default=0, null=True)
    @property
    def valor_res_cons(self, bonus=0):
        if self.res_cons:
            return self.mod_constituicao + self.proficiencia + self.ores_cons
        else:
            return self.mod_constituicao + self.ores_cons

    # INTELIGENCIA
    res_int = models.BooleanField(default=False, null=True)
    ores_int = models.IntegerField(default=0, null=True)
    @property
    def valor_res_int(self, bonus=0):
        if self.res_int:
            return self.mod_inteligencia + self.proficiencia + self.ores_int
        else:
            return self.mod_inteligencia + self.ores_int

    # SABEDORIA
    res_sab = models.BooleanField(default=False, null=True)
    ores_sab = models.IntegerField(default=0, null=True)
    @property
    def valor_res_sab(self, bonus=0):
        if self.res_sab:
            return self.mod_sabedoria + self.proficiencia + self.ores_sab
        else:
            return self.mod_sabedoria + self.ores_sab

    # CARISMA
    res_car = models.BooleanField(default=False, null=True)
    ores_car = models.IntegerField(default=0, null=True)
    @property
    def valor_res_car(self):
        if self.res_car:
            return self.mod_carisma + self.proficiencia + self.ores_car
        else:
            return self.mod_carisma + self.ores_car


    #Pericias
    acrobacia = models.BooleanField(default=False, null=True)
    ot_acrobacia = models.IntegerField(default=0, null=True)
    @property
    def valor_acrobacia(self, bonus=0):
        if self.acrobacia :
            return self.mod_forca + self.proficiencia + self.ot_acrobacia
        else:
            return self.mod_forca

    adestrar_animais = models.BooleanField(default=False, null=True)
    ot_adestrar_animais = models.IntegerField(default=0, null=True)
    @property
    def valor_adestrar_animais(self, bonus=0):
        if self.adestrar_animais:
            return self.mod_carisma + self.proficiencia + self.ot_adestrar_animais
        else:
            return self.mod_carisma

    arcanismo = models.BooleanField(default=False, null=True)
    ot_arcanismo = models.IntegerField(default=0, null=True)
    @property
    def valor_arcanismo(self, bonus=0):
        if self.arcanismo :
            return self.mod_inteligencia + self.proficiencia + self.ot_arcanismo
        else:
            return self.mod_inteligencia

    atletismo = models.BooleanField(default=False, null=True)
    ot_atletismo = models.IntegerField(default=0, null=True)
    @property
    def valor_atletismo(self, bonus=0):
        if self.atletismo :
            return self.mod_forca + self.proficiencia + self.ot_atletismo
        else:
            return self.mod_forca

    atuacao = models.BooleanField(default=False, null=True)
    ot_atuacao = models.IntegerField(default=0, null=True)
    @property
    def valor_atuacao(self, bonus=0):
        if self.atuacao:
            return self.mod_carisma + self.proficiencia + self.ot_atuacao
        else:
            return self.mod_carisma

    enganacao = models.BooleanField(default=False, null=True)
    ot_enganacao = models.IntegerField(default=0, null=True)
    @property
    def valor_enganacao(self, bonus=0, null=True):
        if self.enganacao:
            return self.mod_carisma + self.proficiencia + self.ot_enganacao
        else:
            return self.mod_carisma

    furtividade = models.BooleanField(default=False, null=True)
    ot_furtividade = models.IntegerField(default=0, null=True)
    @property
    def valor_furtividade(self, bonus=0):
        if self.furtividade :
            return self.mod_destreza + self.proficiencia + self.ot_furtividade
        else:
            return self.mod_destreza

    historia = models.BooleanField(default=False, null=True)
    ot_historia = models.IntegerField(default=0, null=True)
    @property
    def valor_historia(self, bonus=0):
        if self.historia :
            return self.mod_inteligencia + self.proficiencia + self.ot_historia
        else:
            return self.mod_inteligencia + self.ot_historia

    intimidacao = models.BooleanField(default=False, null=True)
    ot_intimidacao = models.IntegerField(default=0, null=True)
    @property
    def valor_intimidacao(self, bonus=0):
        if self.intimidacao :
            return self.mod_carisma + self.proficiencia + self.ot_intimidacao
        else:
            return self.mod_carisma

    intuicao = models.BooleanField(default=False, null=True)
    ot_intuicao = models.IntegerField(default=0, null=True)
    @property
    def valor_intuicao(self, bonus=0):
        if self.intuicao :
            return self.mod_sabedoria + self.proficiencia + self.ot_intuicao
        else:
            return self.mod_sabedoria

    investigação = models.BooleanField(default=False, null=True)
    ot_investigação = models.IntegerField(default=0, null=True)
    @property
    def valor_investigação(self, bonus=0):
        if self.investigação :
            return self.mod_inteligencia + self.proficiencia + self.ot_investigação
        else:
            return self.mod_inteligencia

    medicina = models.BooleanField(default=False, null=True)
    ot_medicina = models.IntegerField(default=0, null=True)
    @property
    def valor_medicina(self, bonus=0):
        if self.medicina :
            return self.mod_sabedoria + self.proficiencia + self.ot_medicina
        else:
            return self.mod_sabedoria

    natureza = models.BooleanField(default=False, null=True)
    ot_natureza = models.IntegerField(default=0, null=True)
    @property
    def valor_natureza(self, bonus=0):
        if self.natureza :
            return self.mod_inteligencia + self.proficiencia + self.ot_natureza
        else:
            return self.mod_inteligencia

    percepcao = models.BooleanField(default=False, null=True)
    ot_percepcao = models.IntegerField(default=0, null=True)
    @property
    def valor_percepcao(self, bonus=0):
        if self.sabedoria:
            return self.mod_sabedoria + self.proficiencia + self.ot_percepcao
        else:
            return self.mod_sabedoria + self.ot_percepcao

    persuasao = models.BooleanField(default=False, null=True)
    ot_persuasao = models.IntegerField(default=0, null=True)
    @property
    def valor_persuasao(self, bonus=0):
        if self.persuasao :
            return self.mod_carisma + self.proficiencia + self.ot_persuasao
        else:
            return self.mod_carisma

    prestidigitar = models.BooleanField(default=False, null=True)
    ot_prestidigitar = models.IntegerField(default=0, null=True)
    @property
    def valor_prestidigitar(self, bonus=0):
        if self.prestidigitar :
            return self.mod_destreza + self.proficiencia + self.ot_prestidigitar
        else:
            return self.mod_destreza

    religiao = models.BooleanField(default=False, null=True)
    ot_religiao = models.IntegerField(default=0, null=True)
    @property
    def valor_religiao(self, bonus=0):
        if self.religiao :
            return self.mod_inteligencia + self.proficiencia + self.ot_religiao
        else:
            return self.mod_inteligencia

    sobrevivencia = models.BooleanField(default=False, null=True)
    ot_sobrevivencia = models.IntegerField(default=0, null=True)
    @property
    def valor_sobrevivencia(self, bonus=0):
        if self.sobrevivencia :
            return self.mod_sabedoria + self.proficiencia + self.ot_sobrevivencia
        else:
            return self.mod_sabedoria


class HabilidadesClasse(models.Model):
    personagem = models.ForeignKey('BasePersonagem', on_delete=models.CASCADE)
    habilidade = models.CharField(max_length=30)
    descricao = models.TextField(max_length=999)

    def __str__(self):
        return self.habilidade

class TalentosClasse(models.Model):
    personagem = models.ForeignKey('BasePersonagem', on_delete=models.CASCADE)
    habilidade = models.CharField(max_length=30)
    descricao = models.TextField(max_length=999)

    def __str__(self):
        return self.habilidade

class CaracteristicasRaciaisClasse(models.Model):
    personagem = models.ForeignKey('BasePersonagem', on_delete=models.CASCADE)
    habilidade = models.CharField(max_length=30)
    descricao = models.TextField(max_length=999)

    def __str__(self):
        return self.habilidade

'''
Moeda         pc     pp    pe    po     pl
Cobre    (pc) 1      1/10  1/50  1/100  1/1.000
Prata    (pp) 10     1     1/5   1/10   1/100
Electro  (pe) 50     5     1     1/2    1/20
Ouro     (po) 100    10    2     1      1/10
Platina  (pl) 1.000  100   20    10     1
'''

class InventarioPersonagem(models.Model):
    MOEDAS = [('pc','Cobre'), ('pp','Prata'), ('pe','Electro'), ('po','Ouro'), ('pl','Platina')]
    personagem = models.ForeignKey('BasePersonagem', on_delete=models.CASCADE)
    item_id = models.IntegerField()
    quantidade = models.IntegerField(default=1, null=True, blank=True)
    nome_item = models.CharField(max_length=30)
    valor = models.IntegerField(default=0)
    moeda = models.CharField(max_length=2, choices=MOEDAS)
    peso = models.FloatField(default=0, null=True, blank=True)
    descricao = models.TextField(default='', null=True, blank=True)
    propriedades = models.TextField(default='', null=True, blank=True)
    habilidade = models.TextField(default='', null=True, blank=True)
    
