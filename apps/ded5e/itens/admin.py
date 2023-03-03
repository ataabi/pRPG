from django.contrib import admin
from .models import ItemsComuns, Armaduras, Armas
# Register your models here.
class ListandoItensLoja(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome',)

admin.site.register(ItemsComuns, ListandoItensLoja)

class ListandoArmaduras(admin.ModelAdmin):
    list_display = ('id','nome','ca')
    list_display_links = ('id','nome','ca')

admin.site.register(Armaduras, ListandoArmaduras)

class ListandoArmas(admin.ModelAdmin):
    list_display = ('id','nome','dano')
    list_display_links = ('id','nome','dano')

admin.site.register(Armas,ListandoArmas)
