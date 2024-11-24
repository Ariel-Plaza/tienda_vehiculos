from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            grupo_usuario = Group.objects.get(name = 'Usuario')
            user.groups.add(grupo_usuario)
            return redirect('login')
    else:
        form = RegistroForm()
        return render(request,'usuarios/registro.html',{'form': form})
        
def logout_view(request):
    logout(request)
    messages.success(request,'Has cerrado la sesion')
    return redirect('usuarios:login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'Se ha iniciado sesion con éxito')
        # user1 = request.user
        if request.user.is_superuser:
            grupo =  "Administrador"
        else:
            grupo = request.user.groups.values_list('name', flat=True).first()
        print(grupo)
        request.session['grupo'] = grupo

        return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html',{'form': form })