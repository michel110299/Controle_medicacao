from django.shortcuts import render,redirect
from cadastro.forms import *
from cadastro.models import *
from django.contrib import messages

def registrar_remedio(request):

    form = Remedioform

    todos_remedios = Remedio.objects.all()

    if request.method == "POST":

        form = Remedioform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("home")


    context = {
        "nome_pagina":"Cadastro de remedios",
        "form":form,
        "todos_remedios": todos_remedios,
    }

    return render(request,"cadastro_remedio.html",context)

def registrar_pessoa(request):

    form = Pessoaform
    todas_pessoas = Pessoa.objects.all()

    if request.method == "POST":

        form = Pessoaform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("home")


    context = {
        "nome_pagina":"Cadastro de Pacientes",
        "form":form,
        "todas_pessoas":todas_pessoas,

    }

    return render(request,"cadastro_pessoa.html",context)

def registrar_receita(request):

    form = Receitaform
    todas_receitas = Receita.objects.all()

    if request.method == "POST":

        form = Receitaform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("home")


    context = {
        "nome_pagina" : "Cadastro de receitas",
        "todas_receitas" : todas_receitas,
        "form" : form,
    }
    return render(request,"cadastro_receita.html",context)

def login_usuario(request):

    if request.POST:
        
        cpf_login = request.POST.get('cpf', None)

        try:
            objpessoa = Pessoa.objects.get(cpf=cpf_login)
            return redirect("dashboard_usuario")
            
        except:
            messages.error(request,"Não temos esse cpf cadastrado!")
            return redirect("home")

    context = {
        "nome_pagina" : "Login",
    }
    return render(request,"login_usuario.html",context)

