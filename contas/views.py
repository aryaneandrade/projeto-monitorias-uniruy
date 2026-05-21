
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from contas.forms import RegisterForm, LoginForm


def register_view(request):

    if request.method == 'POST':

        formularo_usuario = RegisterForm(request.POST)

        if formularo_usuario.is_valid():
            formularo_usuario.save()
            messages.success(request, 'Conta criada com sucesso! Agora faça login para acessar o painel.')
            return redirect('login')

    else:
        formularo_usuario = RegisterForm()

    return render(
        request,
        'registro.html',
        {'formularo_usuario': formularo_usuario}
    )


def login_view(request):

    if request.method == 'POST':

        login_form = LoginForm(request, data=request.POST)

        if login_form.is_valid():

            user = login_form.get_user()

            login(request, user)

            return redirect('painel')

    else:
        login_form = LoginForm()

    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )


def logout_view(request):

    logout(request)

    return redirect('monitorias_list')
