from django.contrib import admin
from .models import *
# Register your models here.

class ListandoBasePersonagem(admin.ModelAdmin):
    list_display = ('id','nome_jogador','nome_personagem','nivel')
    list_display_link = ('id','nome_jogador')
    search_fields = ('nome_jogador',)
    list_filter = ('nome_jogador',)
    
admin.site.register(BasePersonagem, ListandoBasePersonagem)

class ListandoHabilidades(admin.ModelAdmin):
    list_display = ('id','personagem','habilidade')
    list_display_links = ('id','personagem',)

admin.site.register(HabilidadesClasse, ListandoHabilidades)

class ListandoTalentos(admin.ModelAdmin):
    list_display = ('id','personagem','habilidade')
    list_display_links = ('id','personagem',)

admin.site.register(TalentosClasse, ListandoTalentos)

class ListandoCaraRaciais(admin.ModelAdmin):
    list_display = ('id','personagem','habilidade')
    list_display_links = ('id','personagem',)

admin.site.register(CaracteristicasRaciaisClasse, ListandoCaraRaciais)

class ListandoInventarioPersonagem(admin.ModelAdmin):
    list_display = ('id','nome_item', 'personagem')
    list_display_links = ('id', 'nome_item', 'personagem',)
    list_filter = ('personagem',)
    

admin.site.register(InventarioPersonagem, ListandoInventarioPersonagem)

