from django.shortcuts import render, HttpResponse, redirect
from .models import BasePersonagem, HabilidadesClasse, TalentosClasse, CaracteristicasRaciaisClasse
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
        print(request.user.username)
        return render(request, 'cria_ficha.html')
    else:
        nome_jogador = request.user.username
        nome_personagem = request.POST['nome_personagem']
        if BasePersonagem.objects.filter(nome_jogador=nome_jogador,nome_personagem=nome_personagem).exists():
            print('Nome de personagem em uso')
            return redirect('criar_ficha')

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
            pv_maximo = request.POST['pvmax'],
            pv_atual = request.POST['pvatual'],
            dados_vida =request.POST['dv'],
            idiomas = request.POST['idiomas'],
            #Habilidades basicas
            forca=request.POST['forca'],
            destreza=request.POST['destreza'],
            constituicao=request.POST['constituicao'],
            inteligencia=request.POST['inteligencia'],
            sabedoria=request.POST['sabedoria'],
            carisma=request.POST['carisma'],
            # Teste de Resistencia 
            res_for = request.POST['tr_for'], ores_for = request.POST['otr_for'],
            res_des = request.POST['tr_des'], ores_des = request.POST['otr_des'],
            res_cons= request.POST['tr_cons'], ores_cons= request.POST['otr_cons'],
            res_int= request.POST['tr_int'], ores_int= request.POST['otr_int'],
            res_sab= request.POST['tr_sab'], ores_sab= request.POST['otr_sab'],
            res_car= request.POST['tr_car'], ores_car= request.POST['otr_car'],
            
            #Pericias
            acrobacia = request.POST.get('acrobacia'), ot_acrobacia = request.POST.get('o_acrobacia'),
            adestrar_animais = request.POST.get('adestrar_animais'),
            ot_adestrar_animais = request.POST.get('o_adestrar_animais'),
            arcanismo = request.POST.get('arcanismo'), ot_arcanismo = request.POST['o_arcanismo'],
            atletismo = request.POST.get('atletismo'), ot_atletismo = request.POST['o_atletismo'],
            atuacao = request.POST.get('atuacao'), ot_atuacao = request.POST['o_atuacao'],
            enganacao = request.POST.get('enganacao'), ot_enganacao = request.POST['o_enganacao'],
            furtividade = request.POST.get('furtividade'), ot_furtividade = request.POST['o_furtividade'],
            historia = request.POST.get('historia'), ot_historia = request.POST['o_historia'],
            intimidacao = request.POST.get('intimidacao'), ot_intimidacao = request.POST['o_intimidacao'],
            intuicao = request.POST.get('intuicao'), ot_intuicao = request.POST['o_intuicao'],
            investigação = request.POST.get('investigação'), ot_investigação = request.POST['o_investigação'],
            medicina = request.POST.get('medicina'), ot_medicina = request.POST['o_medicina'],
            natureza = request.POST.get('natureza'), ot_natureza = request.POST['o_natureza'],
            percepcao = request.POST.get('percepcao'), ot_percepcao = request.POST['o_percepcao'],
            persuasao = request.POST.get('persuasao'), ot_persuasao = request.POST['o_persuasao'],
            prestidigitar = request.POST.get('prestidigitar'), ot_prestidigitar = request.POST['o_prestidigitar'],
            religiao = request.POST.get('religiao'), ot_religiao = request.POST['o_religiao'],
            sobrevivencia = request.POST.get('sobrevivencia'), ot_sobrevivencia = request.POST['o_sobrevivencia'],
        )
        ficha.save()

        personagem = BasePersonagem.objects.filter(nome_personagem=nome_personagem,nome_jogador=nome_jogador).order_by('id').last()
        
        lista_habilidades_c = request.POST.getlist('habilidade_classe')
        for hab in lista_habilidades_c:
            HabilidadesClasse.objects.create(personagem=personagem,habilidade=hab,descricao='teste 123')
        
        lista_talentos = request.POST.getlist('talentos_classe')
        print(lista_talentos)
        for talento in lista_talentos:
            TalentosClasse.objects.create(personagem=personagem,talento=talento,descricao='teste 123')
        
        lista_cara_raciais = request.POST.getlist('cara_raciais_classe')
        print(lista_cara_raciais)
        for cara in lista_cara_raciais:
            CaracteristicasRaciaisClasse.objects.create(personagem=personagem,caracteristica=cara,descricao='teste 123')
        
        return render(request, 'ver_ficha.html')


def ver_ficha(request):
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
    dados = {
        'base':base,
        'habilidades':habilidades,
        'talentos':talentos,
        'cara_raciais':cara_raciais
    }

    return render(request,'ver_ficha.html' ,dados)


def editar_ficha(request):
    jogador = request.user.username
    pid = request.POST.get('pid')
    print(jogador)
    print(pid)
    return redirect('ver_ficha')


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

