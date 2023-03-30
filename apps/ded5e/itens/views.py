from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ded5e.personagem.models import BasePersonagem, InventarioPersonagem
from .models import *

#Loja
@login_required(login_url='/login')
def loja(request):
    """
    View responsável por pegar os itens do banco de dados, pegar os personagens do usuário,
    e exibi-los, também responsável por pegar os itens no inventario do personagem selecionado
    """
    # PID : ID do Personagem
    # IID : ID do Item

    # Pega a lista de itens Comuns
    itens = ItemsComuns.objects.all()
    
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

    return render(request, 'ded5e/loja.html', dados)
    
def inventario(request,nome_personagem):
    """
    View responsável por pegar o inventario de um personagem e exibi-lo
    """
    personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)
    
    personagem = BasePersonagem.objects.get(
            nome_jogador=request.user.username,nome_personagem=nome_personagem
            )
    inventario = InventarioPersonagem.objects.all().filter(personagem=personagem.id)

    return render(request,'ded5e/ver_ficha.html', {
        'inventario':inventario,
        'personagens':personagens,
        'personagem':personagem}
        )

def inventario_update(request,nome_personagem):
    """ 
    view responsavel por encaminha os dados do formulário do usuário para 
    a criação ou alteração do inventario do personagem
    """
    cria_atualiza_inventario(request,nome_personagem)
    return redirect('ver_ficha')

def cria_atualiza_inventario(request,nome_personagem):
    """ Compara o inventario do personagem no servirdor com o 
    inventario do cliente, e faz as modificações necessarias"""

    # PID : ID do Personagem
    # IID : ID do Item

    # Lista os itens pelo nome
    lista_itens = request.POST.getlist('item_nome')
    print('NOMES: ',lista_itens)

    # ID do Personagem
    # nome_personagem = request.POST.get('personagem')
    pid = BasePersonagem.objects.get(
            nome_jogador=request.user.username, nome_personagem=nome_personagem
            ).id 

    # Pegando a lista com a quantidade de cada item
    quantidades = request.POST.getlist('item_quantidade')

    # Pegando o inventario do personagem
    inventario_personagem = InventarioPersonagem.objects.filter(personagem=pid)

    # Verifica qual item deve ser removido do inventario do personagem
    if len(lista_itens) < len(inventario_personagem):
        for item in inventario_personagem:
            if item.nome_item not in lista_itens:
                item.delete()

    # Pegando os dados do lado do cliente, transformando-os em listas
    # e passando para o inventario do jogador
    for item, quantidade in zip(lista_itens,quantidades):
        try:
            db_item = ItemsComuns.objects.get(nome=item)
            print(db_item.nome, quantidade)
            print('Descrição: ', db_item.descricao, '\n')
            informacoes = {
                'personagem': BasePersonagem.objects.get(pk=pid),
                'item_id':db_item.id,
                'quantidade' : quantidade,
                'valor': db_item.valor,
                'moeda': db_item.moeda, 
                'peso': db_item.peso, 
                'descricao': db_item.descricao,
                'propriedades': db_item.propriedades,
                'habilidade': db_item.habilidade,
            }
            print('Informações passadas com sucesso')
        except:
            print('Item não encontrado')
            informacoes = {
                'personagem': BasePersonagem.objects.get(pk=pid),
                'quantidade' : quantidade,
            }

        item, status = InventarioPersonagem.objects.update_or_create(
            nome_item=item,defaults=informacoes
        )


def equipamentos(request, nome_personagem):
    """
    View responsável por buscar as armas e armaduras associadas ao personagem escolhido pelo usuário
    """
    jogador = request.user.username
    personagens = BasePersonagem.objects.filter(nome_jogador=jogador)

    personagem = BasePersonagem.objects.get(nome_jogador=jogador, nome_personagem=nome_personagem)
    
    armas = Armas.objects.filter(personagem=personagem)
    armaduras = Armaduras.objects.filter(personagem=personagem)

    dados = {
        'personagens':personagens,
        'armas':armas,
        'armaduras':armaduras,
        'nome_personagem':nome_personagem
    }
    return render(request, 'ded5e/ver_ficha.html', dados)      

def add_armadura(request, nome_personagem):
    """  
    View renponsável por pegas as informações do formulário e adicionar uma armadura ao
    personagem selecionado pelo usuário
    """
    personagem = BasePersonagem.objects.get(
        nome_personagem=nome_personagem,nome_jogador=request.user.username)
    nome = request.POST.get('nome_armadura')
    preco = request.POST.get('preco_armadura')
    moeda = request.POST.get('moeda_armadura')
    peso = request.POST.get('peso_armadura')
    descricao = request.POST.get('descricao_armadura')
    ca = request.POST.get('ca_armadura')
    forca = request.POST.get('forca_armadura')
    furtividade = request.POST.get('Furtividade_armadura')
    categoria = request.POST.get('categoria_armadura')

    Armaduras.objects.create(
        personagem=personagem,
        nome=nome,
        preco=preco,
        moeda=moeda,
        peso=peso,
        descricao=descricao,
        ca=ca,
        forca=forca,
        furtividade=furtividade,
        categoria=categoria).save()

    return redirect('equipamentos',nome_personagem)

def remover_armadura(request, nome_personagem, id):
    """ 
    View responsável por remover uma armadura de um personagem 
    selecionada pelo usuário
    """
    Armaduras.objects.get(pk=id).delete()
    return redirect('equipamentos', nome_personagem)

def add_arma(request, nome_personagem):
    """  
    View renponsável por pegas as informações do formulário e adicionar uma arma ao
    personagem selecionado pelo usuário
    """
    personagem = BasePersonagem.objects.get(
        nome_personagem=nome_personagem,nome_jogador=request.user.username)
    nome = request.POST.get('nome_arma')
    preco = request.POST.get('preco_arma')
    moeda = request.POST.get('moeda_arma')
    peso = request.POST.get('peso_arma')
    descricao = request.POST.get('descricao_arma')
    dano = request.POST.get('dano_arma')
    propriedades = request.POST.get('propriedades_arma')

    Armas.objects.create(
        personagem=personagem,
        nome=nome,
        preco=preco,
        moeda=moeda,
        peso=peso,
        descricao=descricao,
        dano=dano,
        propriedades=propriedades
        ).save()  

    return redirect('equipamentos',nome_personagem)       

def remover_arma(request, nome_personagem, id):
    """ 
    View responsável por remover uma arma de um personagem 
    selecionada pelo usuário
    """
    Armas.objects.get(pk=id).delete()
    return redirect('equipamentos', nome_personagem)

def cria_atualiza_inventario2(request):

    """ Compara o inventario do personagem no servirdor com o 
    inventario do cliente, e faz as modificações necessarias"""

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
        item_servidor = ItemsComuns.objects.get(pk=iid)

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
                