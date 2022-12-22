from django.contrib import admin
from .models import BasePersonagem, HabilidadesClasse, TalentosClasse, CaracteristicasRaciaisClasse

# Register your models here.

class ListandoBasePersonagem(admin.ModelAdmin):
    list_display = ('id','nome_jogador','nome_personagem','nivel')
    list_display_link = ('id','nome_jogador')
    search_fields = ('nome_jogador',)
    
admin.site.register(BasePersonagem, ListandoBasePersonagem)

class ListandoHabilidades(admin.ModelAdmin):
    list_display = ('id','personagem','habilidade')
    list_display_links = ('id','personagem',)

admin.site.register(HabilidadesClasse, ListandoHabilidades)

class ListandoTalentos(admin.ModelAdmin):
    list_display = ('id','personagem','talento')
    list_display_links = ('id','personagem',)

admin.site.register(TalentosClasse, ListandoTalentos)

class ListandoCaraRaciais(admin.ModelAdmin):
    list_display = ('id','personagem','caracteristica')
    list_display_links = ('id','personagem',)

admin.site.register(CaracteristicasRaciaisClasse, ListandoCaraRaciais)