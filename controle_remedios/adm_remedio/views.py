from django.shortcuts import render ,redirect
from cadastro.models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from adm_remedio.models import Agenda_receita,Horario_remedio
from datetime import date


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

    horarios_remedios = timezone.now()
    horario_atual = timezone.now()
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    objReceita = Receita.objects.get(pk=id_receita)


    try: 
        objAgenda_receita = Agenda_receita.objects.get(receita=objReceita)
        
    except Agenda_receita.DoesNotExist:
        print("nao existe") 
        objAgenda_receita = Agenda_receita()
        objAgenda_receita.receita = objReceita
        objAgenda_receita.nome_completo = "receita"
        objAgenda_receita.data_inicio = horarios_remedios        
        objAgenda_receita.data_de_termino = horarios_remedios + timezone.timedelta(days=objReceita.quantidade_dias)
        objAgenda_receita.save()
        totalDoze = int((objReceita.quantidade_dias*24)/objReceita.intervalo)
        
        objHorario = Horario_remedio()
        objHorario.agenda_receita = objAgenda_receita
        objHorario.horario = horarios_remedios
        objHorario.save()
        
        for q in range(totalDoze):
            horarios_remedios += timezone.timedelta(hours=objReceita.intervalo)
            objHorario = Horario_remedio()
            objHorario.agenda_receita = objAgenda_receita
            objHorario.horario = horarios_remedios
            objHorario.save()


    listHorario = Horario_remedio.objects.filter(agenda_receita=objAgenda_receita)
        
        
    objAgenda_receita.save()



    if request.POST:
        idObjHorario = request.POST.get('tomou_remedio', None)
        if idObjHorario:
            objHorario = Horario_remedio.objects.get(pk=idObjHorario)
            objHorario.concluido = True
            objHorario.save()
            return redirect("dashboard_usuario")
        else:
            return redirect("dashboard_usuario")


    context = {
        "nome_pagina":"Dosagens",
        "usuario" : objPessoa,
        "objAgenda_receita" : objAgenda_receita,
        'listHorario':listHorario,
        'horario_atual' : horario_atual,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request):


    context = {
        "nome_pagina":"Configurar horários",
        "usuario" : objPessoa,
    }

    return render(request,"configura_horarios.html",context)



