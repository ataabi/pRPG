from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    
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
        return render(request, 'usuarios/login.html')

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

def altera_senha(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        email_usuario = request.POST.get('email_usuario')
        dados = {'nome':nome_usuario,'email':email_usuario}

        if User.objects.filter(username=nome_usuario).exists():
            try:
                usuario = User.objects.get(username=nome_usuario)
                if usuario.email == email_usuario:
                    senha1 = request.POST['senha1']
                    senha2 = request.POST['senha2']
                    if senha1 == senha2:
                        usuario.set_password(senha1)
                        usuario.save()
                        return redirect('login_view')
            except:
                return render(request, 'usuarios/mudar_senha.html', dados)

    return render(request, 'usuarios/mudar_senha.html')
