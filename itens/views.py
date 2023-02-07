from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from personagem.models import BasePersonagem, InventarioPersonagem
from .models import *

# Create your views here.

#Loja
@login_required(login_url='/login')
def loja(request):
    # PID : ID do Personagem
    # IID : ID do Item

    # Pega a lista de itens Comuns
    itens = EquipamentoAventura.objects.all()
    
    # Pega os personagens do jogador
    personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)
    
    dados = {
        "itens":itens,
        'personagens':personagens
        }

    if 'personagem' in request.GET:
        # Pegando o Personagem escolhido
        personagem = request.GET.get('personagem')
        pid = BasePersonagem.objects.get(
            nome_jogador=request.user.username, nome_personagem=personagem
            ).id
        # Pegando o inventario do personagem
        inventario = InventarioPersonagem.objects.filter(personagem=pid)
        dados['inventario'] = inventario
        dados['personagem'] = personagem
        # dados['moeda_personagem'] = personagem.

    if request.method == 'POST':
        cria_atualiza_inventario(request)
        # quantidades = request.POST.getlist('itemQuantidade')

        # # lista de ids dos itens do cliente
        # iid_itens = request.POST.getlist('iid')

        # # ID do Personagem
        # personagem = request.POST.get('personagem')
        # pid = BasePersonagem.objects.get(
        #     nome_jogador=request.user.username, nome_personagem=personagem
        #     ).id 
        # inventario_personagem = InventarioPersonagem.objects.filter(personagem=pid)

        # if len(iid_itens) < len(inventario_personagem):
        #     for item in inventario_personagem:
        #         if str(item.item_id) not in iid_itens:
        #             item.delete()
        # for iid, quantidade in zip(iid_itens,quantidades):
        #     iid = int(iid)
        #     item_servidor = EquipamentoAventura.objects.get(pk=iid)

        #     try:
        #         item_cliente = inventario_personagem.get(item_id=iid)
        #         if item_cliente.item_id == item_servidor.id:
        #             InventarioPersonagem.objects.filter(pk=item_cliente.id).update(
        #                 quantidade=quantidade)
        #     except:
        #         InventarioPersonagem.objects.create(
        #             personagem=BasePersonagem.objects.get(pk=pid),
        #             quantidade=quantidade,
        #             nome_item = item_servidor.nome,
        #             item_id = iid,
        #             valor = item_servidor.valor,
        #             moeda = item_servidor.moeda,
        #             peso = item_servidor.peso,
        #             descricao = item_servidor.descricao,
        #             propriedades = item_servidor.propriedades,
        #             habilidade = item_servidor.habilidade)

    return render(request, 'loja.html', dados)
    

def inventario(request):

    personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)
    
    personagem = BasePersonagem.objects.get(
            nome_jogador=request.user.username,nome_personagem=request.GET.get('personagem')
            )
    inventario = InventarioPersonagem.objects.all().filter(personagem=personagem.id)

    return render(request,'ver_ficha.html', {
        'inventario':inventario,
        'personagens':personagens,
        'personagem':personagem}
        )

def inventario_update(request):
    cria_atualiza_inventario(request)
    return redirect('ver_ficha')


def cria_atualiza_inventario(request):
    """ Cria ou atualiza o inventario de um personagem """

    # PID : ID do Personagem
    # IID : ID do Item

    # lista de ids dos itens do cliente
    iid_itens = request.POST.getlist('iid')

    # ID do Personagem
    nome_personagem = request.POST.get('personagem')
    pid = BasePersonagem.objects.get(
            nome_jogador=request.user.username, nome_personagem=nome_personagem
            ).id 

    quantidades = request.POST.getlist('itemQuantidade')

    inventario_personagem = InventarioPersonagem.objects.filter(personagem=pid)

    if len(iid_itens) < len(inventario_personagem):
        for item in inventario_personagem:
            if str(item.item_id) not in iid_itens:
                item.delete()

    for iid, quantidade in zip(iid_itens,quantidades):
        iid = int(iid)
        item_servidor = EquipamentoAventura.objects.get(pk=iid)

        try:
            item_cliente = inventario_personagem.get(item_id=iid)
            # Verifica se o item do cliente tem o mesmo ID do servidor
            if item_cliente.item_id == item_servidor.id:
                InventarioPersonagem.objects.filter(pk=item_cliente.id,nome_item=item_servidor.nome).update(
                    quantidade=quantidade)
        except:
            InventarioPersonagem.objects.create(
                personagem=BasePersonagem.objects.get(pk=pid),
                quantidade=quantidade,
                nome_item = item_servidor.nome,
                item_id = iid,
                valor = item_servidor.valor,
                moeda = item_servidor.moeda,
                peso = item_servidor.peso,
                descricao = item_servidor.descricao,
                propriedades = item_servidor.propriedades,
                habilidade = item_servidor.habilidade)