from django.shortcuts import render
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

    dados = {
        "itens":itens
        }

    if 'pid' in request.GET:
        # Pegando o Personagem escolhido
        pid = request.GET.get('pid')
        # Pegando o inventario do personagem
        inventario = InventarioPersonagem.objects.filter(personagem=pid)
        dados['inventario'] = inventario
        dados['pid'] = pid
    else:
        # Pega os personagens do jogador
        personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)
        dados['personagens'] = personagens

    if request.method == 'POST':
        quantidades = request.POST.getlist('itemQuantidade')
        print(f'Lista Quantidade : [{quantidades}]')
        iid_itens = request.POST.getlist('iid') # lista de ids dos itens do cliente
        print(f'Lista de ID: {iid_itens}')
        pid = int(request.POST.get('pid')) # ID do Personagem
        inventario_personagem = InventarioPersonagem.objects.filter(personagem=pid)

        for item in iid_itens:
            print(type(item))


        if len(iid_itens) < len(inventario_personagem):
            for item in inventario_personagem:
                if str(item.item_id) not in iid_itens:
                    print(f'ID:[{item.item_id}],Nome:[{item.nome_item}], Tipo:[{type(item.item_id)}]')
                    item.delete()

        for iid, quantidade in zip(iid_itens,quantidades):
            iid = int(iid)
            item_servidor = EquipamentoAventura.objects.get(pk=iid)

            try:
                item_cliente = inventario_personagem.get(item_id=iid)
                if item_cliente.item_id == item_servidor.id:
                    InventarioPersonagem.objects.filter(pk=item_cliente.id).update(
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


    return render(request, 'loja.html', dados)
    