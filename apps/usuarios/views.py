from django.shortcuts import render, redirect 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import CadastrarUsuarioForm
from .models import Usuario

def Entrar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('core/inicio.html'))  
        return render(request, 'usuarios/entrar.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('email')
        senha = request.POST.get('password')

        autenticado = authenticate(username=usuario, password=senha)
        if autenticado is not None:
            login(request, autenticado)
            return redirect(reverse('inicio'))
        # TODO Adicionar message de error (Dados errados ou inválidos)
        return render(request, 'usuarios/entrar.html')
    
def Sair(request):
    if request.method == 'GET':
        logout(request)
        return redirect(reverse('inicio'))
    
def CadastrarUsuario(request):
    if request.method == 'POST':
        form = CadastrarUsuarioForm(request.POST or None)
        if form.is_valid():
            nome = form.cleaned_data.get('first_name')
            usuario = form.cleaned_data.get('email')
            telefone = form.cleaned_data.get('telefone')
            senha = form.cleaned_data.get('password')

            if Usuario.objects.filter(username=usuario, is_active=True).exists():
                # TODO Adicionar message de error (Já existe usuário com esté email)
                return redirect(reverse('cadastrar_usuario'))
            Usuario.objects.create_user(first_name=nome, username=usuario, telefone=telefone, password=senha)
           
            autenticado = authenticate(username=usuario, password=senha)
            if autenticado is not None:
                login(request, autenticado)
                return redirect(reverse('inicio'))
                
    return render(request, 'usuarios/cadastrar.html')