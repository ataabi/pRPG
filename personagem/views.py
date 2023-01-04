from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def cria_ficha(request):
    if request.method == 'GET':
        return render(request, 'cria_ficha.html')

    if request.method == 'POST':
        nome_jogador = request.user.username
        nome_personagem = request.POST['nome_personagem']
        if BasePersonagem.objects.filter(nome_jogador=nome_jogador,nome_personagem=nome_personagem).exists():
            messages.add_message(request, messages.INFO, 'Você já possui um personagem com este nome')
            print('Nome de personagem em uso')
            return redirect('cria_ficha')

        ficha = BasePersonagem.objects.create(
            nome_jogador = nome_jogador,
            nome_personagem = nome_personagem,
            raca = request.POST['raca'],
            classe = request.POST['classe'],
            arquetipo = request.POST['arquetipo'],
            nivel = request.POST['nivel'],
            antecedente = request.POST['antecedente'],
            tendencia = request.POST['tendencia'],
            divindade = request.POST['divindade'],
            terra_natal = request.POST['terra_natal'],
            iniciativa = request.POST['iniciativa'],
            c_a = request.POST['c_a'],
            deslocamento = request.POST['deslocamento'],
            inspiracao = request.POST['inspiracao'],
            proficiencia = request.POST['proficiencia'],
            pv_maximo = request.POST['pv_maximo'],
            pv_atual = request.POST['pv_atual'],
            dados_vida =request.POST['dados_vida'],
            idiomas = request.POST['idiomas'],
            #Habilidades basicas
            forca=request.POST['forca'],
            destreza=request.POST['destreza'],
            constituicao=request.POST['constituicao'],
            inteligencia=request.POST['inteligencia'],
            sabedoria=request.POST['sabedoria'],
            carisma=request.POST['carisma'],
            # Teste de Resistencia 
            res_for = request.POST['res_for'], ores_for = request.POST['ores_for'],
            res_des = request.POST['res_des'], ores_des = request.POST['ores_des'],
            res_cons= request.POST['res_cons'], ores_cons= request.POST['ores_cons'],
            res_int= request.POST['res_int'], ores_int= request.POST['ores_int'],
            res_sab= request.POST['res_sab'], ores_sab= request.POST['ores_sab'],
            res_car= request.POST['res_car'], ores_car= request.POST['ores_car'],
            #Pericias
            acrobacia = request.POST.get('acrobacia'), ot_acrobacia = request.POST.get('ot_acrobacia'),
            adestrar_animais = request.POST.get('adestrar_animais'),
            ot_adestrar_animais = request.POST.get('ot_adestrar_animais'),
            arcanismo = request.POST.get('arcanismo'), ot_arcanismo = request.POST['ot_arcanismo'],
            atletismo = request.POST.get('atletismo'), ot_atletismo = request.POST['ot_atletismo'],
            atuacao = request.POST.get('atuacao'), ot_atuacao = request.POST['ot_atuacao'],
            enganacao = request.POST.get('enganacao'), ot_enganacao = request.POST['ot_enganacao'],
            furtividade = request.POST.get('furtividade'), ot_furtividade = request.POST['ot_furtividade'],
            historia = request.POST.get('historia'), ot_historia = request.POST['ot_historia'],
            intimidacao = request.POST.get('intimidacao'), ot_intimidacao = request.POST['ot_intimidacao'],
            intuicao = request.POST.get('intuicao'), ot_intuicao = request.POST['ot_intuicao'],
            investigação = request.POST.get('investigação'), ot_investigação = request.POST['ot_investigação'],
            medicina = request.POST.get('medicina'), ot_medicina = request.POST['ot_medicina'],
            natureza = request.POST.get('natureza'), ot_natureza = request.POST['ot_natureza'],
            percepcao = request.POST.get('percepcao'), ot_percepcao = request.POST['ot_percepcao'],
            persuasao = request.POST.get('persuasao'), ot_persuasao = request.POST['ot_persuasao'],
            prestidigitar = request.POST.get('prestidigitar'), ot_prestidigitar = request.POST['ot_prestidigitar'],
            religiao = request.POST.get('religiao'), ot_religiao = request.POST['ot_religiao'],
            sobrevivencia = request.POST.get('sobrevivencia'), ot_sobrevivencia = request.POST['ot_sobrevivencia'],
        )
        ficha.save()

        personagem = BasePersonagem.objects.get(nome_personagem=nome_personagem,nome_jogador=nome_jogador)

        #Removendo as Habilidades Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,HabilidadesClasse,'habilidade_classe',personagem)

        #Removendo os Talentos Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,TalentosClasse,'talentos_classe',personagem)

        #Removendo as Caracteristicas Raciais Atuais e Recriando com base no cliente
        gerencia_multiplos_elementos(request,CaracteristicasRaciaisClasse,'cara_raciais_classe',personagem)
        
        return render(request, 'ver_ficha.html')



@login_required(login_url='/login')
def ver_ficha(request):
    if 'deletar' in request.POST:
        BasePersonagem.objects.get(pk=request.POST.get("id"),nome_jogador=request.user.username).delete()
    
    try:
        base = BasePersonagem.objects.get(
            nome_jogador=request.user.username,nome_personagem=request.POST.get('personagem')
            )
    except:
        base = BasePersonagem.objects.filter(nome_jogador=request.user.username)
        return render(request, 'personagens.html', {'base':base})

    habilidades = HabilidadesClasse.objects.all().filter(personagem=base.id)
    talentos = TalentosClasse.objects.all().filter(personagem=base.id)
    cara_raciais = CaracteristicasRaciaisClasse.objects.all().filter(personagem=base.id)
    inventario = InventarioPersonagem.objects.all().filter(personagem=base.id)
    
    dados = {
        'base':base,
        'habilidades':habilidades,
        'talentos':talentos,
        'cara_raciais':cara_raciais,
        'inventario':inventario
    }

    return render(request,'ver_ficha.html' ,dados)


@login_required(login_url='/login')
def editar_ficha(request):
    jogador = request.user.username
    pid = request.POST.get('id')
    print('TENDENCIA')
    print(request.POST.get('tendencia'))
    BasePersonagem.objects.filter(pk=pid).update(
            nome_jogador = jogador,
            nome_personagem = request.POST['nome_personagem'],
            raca = request.POST['raca'],
            classe = request.POST['classe'],
            arquetipo = request.POST['arquetipo'],
            nivel = request.POST['nivel'],
            antecedente = request.POST['antecedente'],
            tendencia = request.POST['tendencia'],
            divindade = request.POST['divindade'],
            terra_natal = request.POST['terra_natal'],
            iniciativa = request.POST['iniciativa'],
            c_a = request.POST['c_a'],
            deslocamento = request.POST['deslocamento'],
            inspiracao = request.POST['inspiracao'],
            proficiencia = request.POST['proficiencia'],
            pv_maximo = request.POST['pv_maximo'],
            pv_atual = request.POST['pv_atual'],
            dados_vida =request.POST['dados_vida'],
            idiomas = request.POST['idiomas'],
            #Habilidades basicas
            forca=request.POST['forca'],
            destreza=request.POST['destreza'],
            constituicao=request.POST['constituicao'],
            inteligencia=request.POST['inteligencia'],
            sabedoria=request.POST['sabedoria'],
            carisma=request.POST['carisma'],
            # Teste de Resistencia 
            res_for = request.POST.get('res_for'), ores_for = request.POST['ores_for'],
            res_des = request.POST.get('res_des'), ores_des = request.POST['ores_des'],
            res_cons= request.POST.get('res_cons'), ores_cons= request.POST['ores_cons'],
            res_int= request.POST.get('res_int'), ores_int= request.POST['ores_int'],
            res_sab= request.POST.get('res_sab'), ores_sab= request.POST['ores_sab'],
            res_car= request.POST.get('res_car'), ores_car= request.POST['ores_car'],
            
            #Pericias
            acrobacia = request.POST.get('acrobacia'), ot_acrobacia = request.POST.get('ot_acrobacia'),
            adestrar_animais = request.POST.get('adestrar_animais'),
            ot_adestrar_animais = request.POST.get('ot_adestrar_animais'),
            arcanismo = request.POST.get('arcanismo'), ot_arcanismo = request.POST['ot_arcanismo'],
            atletismo = request.POST.get('atletismo'), ot_atletismo = request.POST['ot_atletismo'],
            atuacao = request.POST.get('atuacao'), ot_atuacao = request.POST['ot_atuacao'],
            enganacao = request.POST.get('enganacao'), ot_enganacao = request.POST['ot_enganacao'],
            furtividade = request.POST.get('furtividade'), ot_furtividade = request.POST['ot_furtividade'],
            historia = request.POST.get('historia'), ot_historia = request.POST['ot_historia'],
            intimidacao = request.POST.get('intimidacao'), ot_intimidacao = request.POST['ot_intimidacao'],
            intuicao = request.POST.get('intuicao'), ot_intuicao = request.POST['ot_intuicao'],
            investigação = request.POST.get('investigação'), ot_investigação = request.POST['ot_investigação'],
            medicina = request.POST.get('medicina'), ot_medicina = request.POST['ot_medicina'],
            natureza = request.POST.get('natureza'), ot_natureza = request.POST['ot_natureza'],
            percepcao = request.POST.get('percepcao'), ot_percepcao = request.POST['ot_percepcao'],
            persuasao = request.POST.get('persuasao'), ot_persuasao = request.POST['ot_persuasao'],
            prestidigitar = request.POST.get('prestidigitar'), ot_prestidigitar = request.POST['ot_prestidigitar'],
            religiao = request.POST.get('religiao'), ot_religiao = request.POST['ot_religiao'],
            sobrevivencia = request.POST.get('sobrevivencia'), ot_sobrevivencia = request.POST['ot_sobrevivencia'],
        )

    personagem = BasePersonagem.objects.get(pk=pid)

    #Removendo as Habilidades Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,HabilidadesClasse,'habilidade_classe',personagem)

    #Removendo os Talentos Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,TalentosClasse,'talentos_classe',personagem)

    #Removendo as Caracteristicas Raciais Atuais e Recriando com base no cliente
    gerencia_multiplos_elementos(request,CaracteristicasRaciaisClasse,'cara_raciais_classe',personagem)

    return redirect('ver_ficha')


#Usuarios
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        apelido_usuario = request.POST.get('apelido_usuario')
        if User.objects.filter(username=apelido_usuario).exists():
            messages.add_message(request, messages.INFO, 'Este Nick já está em uso')
            return redirect('cadastro')

        email_usuario = request.POST.get('email_usuario')    
        if User.objects.filter(email=email_usuario).exists():
            messages.add_message(request, messages.INFO, 'Este Email já está em uso')
            return redirect('cadastro')

        senha1_usuario = request.POST.get('senha1_usuario')
        senha2_usuario = request.POST.get('senha2_usuario')
        if senha1_usuario != senha2_usuario:
            messages.add_message(request, messages.INFO, 'As senhas não coincidence')
            return redirect('cadastro')

        if len(senha1_usuario) < 4:
            messages.add_message(request, messages.INFO, 'A Senha é muito Curta')
            return redirect('cadastro')

        usuario = User.objects.create_user(
            username=apelido_usuario, first_name=nome_usuario, 
            email=email_usuario, password=senha1_usuario
            )
        usuario.save()
        return redirect('login_view')
        

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        senha_usuario = request.POST.get('senha_usuario')
        usuario = authenticate(username=nome_usuario, password=senha_usuario)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            return redirect('login_view')


def logout_view(request):
    logout(request)
    return redirect('index')



# FUNÇÂO
def gerencia_multiplos_elementos(request, objeto, tipo_habilidade, personagem):
    lista_servidor = objeto.objects.filter(personagem=personagem)
    lista_cliente = request.POST.getlist(tipo_habilidade)
    lista_des_cliente = request.POST.getlist(f'des_{tipo_habilidade}')
    # print('Entrou na função')
    # print(len(lista_servidor),len(lista_cliente))
    # print(lista_cliente,lista_des_cliente)

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

# FIM FUNÇÂO

