from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

lista_pericias = [
    'acrobacia', 'adestrar_animais', 'arcanismo', 'atletismo', 'atuacao', 'enganacao',
    'furtividade','historia','intimidacao','intuicao','investigação','medicina',
    'natureza','percepcao','persuasao','prestidigitar','religiao','sobrevivencia'
]

def index(request):
    teste = FormTeste()
    return render(request, 'index.html', {'teste':teste})

@login_required(login_url='/login')
def cria_ficha(request):
    
    if request.method == 'GET':
        return render(request, 'ded5e/cria_ficha.html', {'lista_pericias':lista_pericias})

    if request.method == 'POST':
        nome_jogador = request.user.username
        nome_personagem = request.POST['nome_personagem']
        
        if BasePersonagem.objects.filter(
            nome_jogador=nome_jogador,
            nome_personagem=nome_personagem
            ).exists():
            messages.add_message(
                request, messages.INFO, 'Você já possui um personagem com este nome'
                )
            print('Nome de personagem em uso')
            return redirect('cria_ficha')

        cria_atualiza_ficha(request)

        personagem = BasePersonagem.objects.get(nome_personagem=nome_personagem,nome_jogador=nome_jogador)

        #Removendo as Habilidades Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,HabilidadesClasse,'habilidade_classe',personagem)

        #Removendo os Talentos Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,TalentosClasse,'talentos_classe',personagem)

        #Removendo as Caracteristicas Raciais Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,CaracteristicasRaciaisClasse,'cara_raciais_classe',personagem)
        
        return redirect('ver_ficha')

@login_required(login_url='/login')
def ver_ficha(request):
    jogador = request.user.username
    personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)
    
    dados = {
            'personagens':personagens,
            'lista_pericias':lista_pericias
        }
    if 'personagem' in request.GET:
        personagem = BasePersonagem.objects.get(
            nome_jogador=jogador,nome_personagem=request.GET.get('personagem')
            )
        dicionario_pericias = {}
        for pericia in lista_pericias:
            status = getattr(personagem, pericia)
            bonus = getattr(personagem, f'bonus_{pericia}')
            dicionario_pericias[pericia] = (status,bonus)


        dados['base'] = personagem
        dados['dicionario_pericias'] = dicionario_pericias
        dados['habilidades'] = HabilidadesClasse.objects.all().filter(personagem=personagem.id)
        dados['talentos'] = TalentosClasse.objects.all().filter(personagem=personagem.id)
        dados['cara_raciais'] = CaracteristicasRaciaisClasse.objects.all().filter(personagem=personagem.id)

    return render(request,'ded5e/ver_ficha.html' ,dados)

    # try:
    #     personagem = BasePersonagem.objects.get(
    #         nome_jogador=request.user.username,nome_personagem=request.POST.get('personagem')
    #         )
    # except:
    #     personagens = 
    #     return render(request, 'personagens.html', {'base':base})

    # habilidades = HabilidadesClasse.objects.all().filter(personagem=base.id)
    # talentos = TalentosClasse.objects.all().filter(personagem=base.id)
    # cara_raciais = CaracteristicasRaciaisClasse.objects.all().filter(personagem=base.id)
    # inventario = InventarioPersonagem.objects.all().filter(personagem=base.id)
    
    # dados = {
    #     'base':personagem,
    #     'habilidades':habilidades,
    #     'talentos':talentos,
    #     'cara_raciais':cara_raciais,
    #     'inventario':inventario
    # }

    # return render(request,'ver_ficha.html' ,dados)

@login_required(login_url='/login')
def editar_ficha(request):
    jogador = request.user.username
    nome_personagem = request.POST['nome_personagem']
    
    cria_atualiza_ficha(request)

    personagem = BasePersonagem.objects.get(
        nome_jogador=jogador,
        nome_personagem=nome_personagem)

    #Removendo as Habilidades Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,HabilidadesClasse,'habilidade_classe',personagem)

    #Removendo os Talentos Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,TalentosClasse,'talentos_classe',personagem)

    #Removendo as Caracteristicas Raciais Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,CaracteristicasRaciaisClasse,'cara_raciais_classe',personagem)

    return redirect('ver_ficha')

@login_required(login_url='/login')
def deletar_ficha(request):
    jogador = request.user.username
    personagem = request.GET.get('personagem')
    id = BasePersonagem.objects.get(nome_personagem=personagem,nome_jogador=jogador).id
    BasePersonagem.objects.get(id=id,nome_jogador=jogador).delete()
    
    return redirect('ver_ficha')


# Magias
@login_required(login_url='/login')
def ver_magias(request, nome_personagem):
    
    jogador = request.user.username
    personagens = BasePersonagem.objects.filter(nome_jogador=request.user.username)

    personagem = get_object_or_404(
        BasePersonagem,nome_personagem=nome_personagem, nome_jogador=jogador)

    lista_magias = MagiasPersonagem.objects.filter(personagem=personagem.id)
    
    dados = {
        'nome_personagem': nome_personagem,
        'personagens': personagens,
        'magias': lista_magias
        }

    return render(request, 'ded5e/ver_ficha.html', dados)

@login_required(login_url='/login')
def adicionar_magia(request,nome_personagem):

    personagem = BasePersonagem.objects.get(
        nome_jogador = request.user.username,
        nome_personagem = nome_personagem
        )

    nome = request.POST.get('nome_magia')
    nivel = request.POST.get('nivel_magia')
    escola = request.POST.get('escola_magia')
    tempo_conjuracao = request.POST.get('tempo_conjuracao_magia')
    alcance = request.POST.get('alcance_magia')
    componentes = request.POST.get('componentes_magia')
    duracao = request.POST.get('duracao_magia')
    descricao = request.POST.get('descricao_magia')

    MagiasPersonagem.objects.create(
        personagem = personagem,
        nome = nome,
        nivel = nivel,
        tempo_conjuracao = tempo_conjuracao,
        alcance = alcance,
        componentes = componentes,
        duracao = duracao,
        descricao = descricao,
        escola = escola
    )

    print('Magia Adicionada')
    return redirect('ver_magias',nome_personagem)

@login_required(login_url='/login')
def remover_magia(request,nome_personagem,id):
    MagiasPersonagem.objects.get(pk=id).delete()
    return redirect(f'ver_magias',nome_personagem)


# FUNÇÕES
def gerencia_multiplos_elementos(request, objeto, tipo_habilidade, personagem):
    lista_servidor = objeto.objects.filter(personagem=personagem)
    lista_cliente = request.POST.getlist(tipo_habilidade)
    lista_des_cliente = request.POST.getlist(f'des_{tipo_habilidade}')

    #Sincronizando a lista de cliente com a do servidor, removendo oque o cliente removeu
    if len(lista_servidor) > len(lista_cliente):
        for item in lista_servidor:
            if str(item) not in lista_cliente:
                objeto.objects.get(personagem=personagem,pk=item.id).delete()       
    
    #Adicionando os itens do cliente ao servidor
    for item,des in zip(lista_cliente,lista_des_cliente):
        item,des = str(item),str(des)
        if not item in str(lista_servidor):
            objeto.objects.create(personagem=personagem,habilidade=item,descricao=des)

def cria_atualiza_ficha(request):
    nome_jogador = request.user.username
    nome_personagem = request.POST['nome_personagem']

    print('RESDES',request.POST.get('res_des'))

    informacoes = {
        'raca':request.POST['raca'],
        'classe':request.POST['classe'],
        'arquetipo':request.POST['arquetipo'],
        'nivel':request.POST['nivel'],
        'antecedente':request.POST['antecedente'],
        'tendencia':request.POST['tendencia'],
        'divindade':request.POST['divindade'],
        'terra_natal':request.POST['terra_natal'],
        'iniciativa':request.POST['iniciativa'],
        'c_a':request.POST['c_a'],
        'deslocamento':request.POST['deslocamento'],
        'inspiracao':request.POST['inspiracao'],
        'proficiencia':request.POST['proficiencia'],
        'pv_maximo':request.POST['pv_maximo'],
        'pv_atual':request.POST['pv_atual'],
        'dados_vida':request.POST['dados_vida'],
        'idiomas':request.POST['idiomas'],
        #Habilidades basicas
        'forca':request.POST['forca'],
        'destreza':request.POST['destreza'],
        'constituicao':request.POST['constituicao'],
        'inteligencia':request.POST['inteligencia'],
        'sabedoria':request.POST['sabedoria'],
        'carisma':request.POST['carisma'],
        # Teste de Resistencia 
        'res_for' : request.POST.get('res_for'), 'bonus_res_for' : request.POST.get('bonus_res_for'),
        'res_des' : request.POST.get('res_des'), 'bonus_res_des' : request.POST.get('bonus_res_des'),
        'res_cons': request.POST.get('res_cons'), 'bonus_res_cons': request.POST.get('bonus_res_cons'),
        'res_int': request.POST.get('res_int'), 'bonus_res_int': request.POST.get('bonus_res_int'),
        'res_sab': request.POST.get('res_sab'), 'bonus_res_sab': request.POST.get('bonus_res_sab'),
        'res_car': request.POST.get('res_car'), 'bonus_res_car': request.POST.get('bonus_res_car'),
        #Pericias
        'acrobacia' : request.POST.get('acrobacia'), 'bonus_acrobacia' : request.POST.get('bonus_acrobacia'),
        'adestrar_animais' : request.POST.get('adestrar_animais'),
        'bonus_adestrar_animais' : request.POST.get('bonus_adestrar_animais'),
        'arcanismo' : request.POST.get('arcanismo'), 'bonus_arcanismo' : request.POST.get('bonus_arcanismo'),
        'atletismo' : request.POST.get('atletismo'), 'bonus_atletismo' : request.POST.get('bonus_atletismo'),
        'atuacao' : request.POST.get('atuacao'), 'bonus_atuacao' : request.POST.get('bonus_atuacao'),
        'enganacao' : request.POST.get('enganacao'), 'bonus_enganacao' : request.POST.get('bonus_enganacao'),
        'furtividade' : request.POST.get('furtividade'), 'bonus_furtividade' : request.POST.get('bonus_furtividade'),
        'historia' : request.POST.get('historia'), 'bonus_historia' : request.POST.get('bonus_historia'),
        'intimidacao' : request.POST.get('intimidacao'), 'bonus_intimidacao' : request.POST.get('bonus_intimidacao'),
        'intuicao' : request.POST.get('intuicao'), 'bonus_intuicao' : request.POST.get('bonus_intuicao'),
        'investigação' : request.POST.get('investigação'), 'bonus_investigação' : request.POST.get('bonus_investigação'),
        'medicina' : request.POST.get('medicina'), 'bonus_medicina' : request.POST.get('bonus_medicina'),
        'natureza' : request.POST.get('natureza'), 'bonus_natureza' : request.POST.get('bonus_natureza'),
        'percepcao' : request.POST.get('percepcao'), 'bonus_percepcao' : request.POST.get('bonus_percepcao'),
        'persuasao' : request.POST.get('persuasao'), 'bonus_persuasao' : request.POST.get('bonus_persuasao'),
        'prestidigitar' : request.POST.get('prestidigitar'), 'bonus_prestidigitar' : request.POST.get('bonus_prestidigitar'),
        'religiao' : request.POST.get('religiao'), 'bonus_religiao' : request.POST.get('bonus_religiao'),
        'sobrevivencia' : request.POST.get('sobrevivencia'), 'bonus_sobrevivencia' : request.POST.get('bonus_sobrevivencia'),
    }
    
    ficha, status = BasePersonagem.objects.update_or_create(
        nome_jogador = nome_jogador,
        nome_personagem = nome_personagem,
        defaults=informacoes
        )

    print(status)
