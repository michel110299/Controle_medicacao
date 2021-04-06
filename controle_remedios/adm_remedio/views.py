from django.shortcuts import render ,redirect
from cadastro.models import *
from django.contrib.auth.decorators import login_required


@login_required
def dashbord_usuario(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    
    context = {
        "nome_pagina": "dashboard",
        "usuario" : objPessoa,
    }

    return render(request,"dashboard_usuario.html",context)

@login_required    
def dosagem_usuario(request,id_receita):

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    
    try:
        objReceita = Receita.objects.get(pessoa=objPessoa)
    except:
        return redirect("dashboard_usuario") 
    try:
        print("44444o22i")  
        objAgenda_receita = Agenda_receita.objects.get(receita = objReceita)
    except:
        objAgenda_receita = Agenda_receita()
        objAgenda_receita.receita = objReceita
        objAgenda_receita.nome_completo = nome
        objAgenda_receita.data_inicio = data_de_inicio
        objAgenda_receita.data_termino = data_de_termino
        
    objAgenda_receita.save()
    
    try:
        objReceita = Receita.objects.get(pessoa=objPessoa)
    except:
        return redirect("dashboard_usuario") 
    if request.method == "POST":
        try:
            print("44444o22i")  
            objAgenda_receita = Agenda_receita.objects.get(receita = objReceita)
        except:

            objAgenda_receita = Agenda_receita()
            objAgenda_receita.receita = objReceita
            objAgenda_receita.nome_completo = nome
            objAgenda_receita.data_inicio = data_de_inicio
            objAgenda_receita.data_termino = data_de_termino
            
        objAgenda_receita.save()


    context = {
        "nome_pagina":"Dosagens",
        "usuario" : objPessoa,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request):

    objPessoa = Pessoa.objects.get(pk=request.user.id)
    
    try:
        objReceita = Receita.objects.get(pessoa=objPessoa)
    except:
        return redirect("dashboard_usuario") 
    if request.method == "POST":
        try:
            print("44444o22i")  
            objAgenda_receita = Agenda_receita.objects.get(receita = objReceita)
        except:

            objAgenda_receita = Agenda_receita()
            objAgenda_receita.receita = objReceita
            objAgenda_receita.nome_completo = nome
            objAgenda_receita.data_inicio = data_de_inicio
            objAgenda_receita.data_termino = data_de_termino
            
        objAgenda_receita.save()


    context = {
        "nome_pagina":"Configurar horários",
        "usuario" : objPessoa,
    }

    return render(request,"configura_horarios.html",context)



