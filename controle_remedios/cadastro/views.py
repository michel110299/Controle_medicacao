from django.shortcuts import render,redirect
from cadastro.forms import *
from cadastro.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adm_remedio.models import *
from django.utils import timezone
from datetime import date
@login_required
def registrar_remedio(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]

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
        "usuario" : primeiro_nome,
    }

    return render(request,"cadastro_remedio.html",context)



def registrar_pessoa(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]
    form = Pessoaform
    todas_pessoas = Pessoa.objects.all()

    if request.method == "POST":

        form = Pessoaform(request.POST)

        if form.is_valid():

            form.save()
            return redirect("login")


    context = {
        "nome_pagina":"Cadastro de Pacientes",
        "form":form,
        "todas_pessoas":todas_pessoas,
        "usuario" : primeiro_nome,

    }

    return render(request,"cadastro_pessoa.html",context)
@login_required
def registrar_receita(request):

    horario_atual = timezone.now()
    data_atual = horario_atual.date()

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]

    form = Receitaform
    list_receitas = Receita.objects.filter(pessoa=objPessoa).order_by("-pk")
    listReceitas = []
    for q in list_receitas:
        try:
            objAgenda = Agenda_receita.objects.get(receita=q)
        except Agenda_receita.DoesNotExist:
            objAgenda = None
            
        obj = {
            "Receita":q,
            "Agenda":objAgenda,
        }
        listReceitas.append(obj)


    if request.method == "POST":

        form = Receitaform(request.POST)


        if form.is_valid():

            receita = form.save(commit = False)
            receita.pessoa = objPessoa
            receita.save()
            return redirect("dashboard_usuario")


    context = {
        "nome_pagina" : "Cadastro de receitas",
        "list_receitas" : listReceitas,
        "form" : form,
        "usuario" : primeiro_nome,
        "data_atual" : data_atual,
    }
    
    return render(request,"cadastro_receita.html",context)


