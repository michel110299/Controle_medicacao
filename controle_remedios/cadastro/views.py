from django.shortcuts import render,redirect
from cadastro.forms import *
from cadastro.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def registrar_remedio(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)

    form = Remedioform
    
    todos_remedios = Remedio.objects.all()

    if request.method == "POST":

        form = Remedioform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("dashboard_usuario")


    context = {
        "nome_pagina":"Cadastro de remedios",
        "form":form,
        "todos_remedios": todos_remedios,
        "usuario" : objPessoa,
    }

    return render(request,"cadastro_remedio.html",context)



def registrar_pessoa(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)

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
        "usuario" : objPessoa,

    }

    return render(request,"cadastro_pessoa.html",context)
@login_required
def registrar_receita(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)

    form = Receitaform
    list_receitas = Receita.objects.filter(pessoa=objPessoa)

    if request.method == "POST":

        form = Receitaform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("dashboard_usuario")


    context = {
        "nome_pagina" : "Cadastro de receitas",
        "list_receitas" : list_receitas,
        "form" : form,
        "usuario" : objPessoa,
    }
    
    return render(request,"cadastro_receita.html",context)


