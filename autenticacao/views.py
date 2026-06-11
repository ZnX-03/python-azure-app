from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.middleware.csrf import rotate_token
from .forms import LoginForm, CriarUsuarioForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('listar_cursos')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Garante que o CSRF token seja renovado antes do redirect
                rotate_token(request)
                return redirect('listar_cursos')
    else:
        form = LoginForm(request)

    return render(request, 'autenticacao/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')


def criar_usuario(request):
    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return render(request, 'autenticacao/criar_usuario.html', {
                'form': CriarUsuarioForm(),
                'sucesso': f'Usuário "{username}" criado com sucesso!'
            })
    else:
        form = CriarUsuarioForm()

    return render(request, 'autenticacao/criar_usuario.html', {'form': form})
