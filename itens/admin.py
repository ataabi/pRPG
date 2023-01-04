from django.contrib import admin
from .models import EquipamentoAventura
# Register your models here.
class ListandoItensLoja(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome',)
    def __str__(self):
        return 'Itens da Loja'

admin.site.register(EquipamentoAventura, ListandoItensLoja)

