from django.shortcuts import render ,redirect
from cadastro.models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from adm_remedio.models import Agenda_receita,Horario_remedio
import datetime
from django.contrib import messages


@login_required
def dashbord_usuario(request):
    horario_atual = timezone.now()
    data_atual = horario_atual.date()
    data_now = timezone.now()
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]
    listReceita = [] 
    listReceitas = []
    listNao_tomado = []
    horario_nao_tomado = 0
    try:
        listReceita = Receita.objects.filter(pessoa=objPessoa)

    except:
        listReceita = None
    


    
    for q in listReceita:
        try:
            objAgenda_receita = Agenda_receita.objects.get(receita=q)
            listHorarios = Horario_remedio.objects.filter(agenda_receita=objAgenda_receita)
            for x in listHorarios:
                if x.concluido == False:
                    if x.horario <= data_now:
                        horario_nao_tomado += 1

            listNao_tomado.append(horario_nao_tomado)
            horario_nao_tomado = 0
            


        except Agenda_receita.DoesNotExist:
            objAgenda_receita = None
            
        obj = {
            "Receita":q,
            "Agenda":objAgenda_receita,
            "listNao_tomado":listNao_tomado,
        }
        
        listReceitas.append(obj)

    for x in listNao_tomado:
        print(x)
    context = {
        "nome_pagina": "dashboard",
        "usuario" :primeiro_nome,
        "listReceitas":listReceitas,
        "data_atual" : data_atual,
        }

    return render(request,"dashboard_usuario.html",context)

@login_required    
def dosagem_usuario(request,id_receita):
    horario_inicio_remedio = timezone.now()
    horario_atual = timezone.now()
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]
    objReceita = Receita.objects.get(pk=id_receita)
    objAgenda_receita = Agenda_receita.objects.get(receita=objReceita)
    nome_pagina = objReceita.remedio.nome_completo
    listHorario = Horario_remedio.objects.filter(agenda_receita=objAgenda_receita)

    listHorarios_false = []

    for l in listHorario:
        if l.concluido == False:
            listHorarios_false.append(l)
    cont = 0 
    for l in listHorarios_false:
        if l.horario <= horario_atual:
            cont += 1

    if cont > 1:

        print("deu ruim")
        messages.error(request,"Voc?? n??o tomou sua ultima dose no hor??rio certo, Por favor selecione uma nova data!") 

        for l in listHorarios_false:
            l.delete()
        
        return redirect("configura_horario_dosagem",id_receita )     
        

        
    else:
        print("est?? certo")
        if request.POST:
            idObjHorario = request.POST.get('tomou_remedio', None)
            if idObjHorario:
                objHorario = Horario_remedio.objects.get(pk=idObjHorario)
                objHorario.concluido = True
                objHorario.save()
                if objHorario == Horario_remedio.objects.filter(agenda_receita=objAgenda_receita).last():
                    print("testekak")
                    objAgenda_receita.concluido = True
                    objAgenda_receita.save()
                return redirect("registrar_receita")
            else:
                return redirect("registrar_receita")


    context = {
        "nome_pagina": "Dosagens - "+ nome_pagina,
        "usuario" : primeiro_nome,
        "objAgenda_receita" : objAgenda_receita,
        'listHorario':listHorario,
        'horario_atual' : horario_atual,
    }

    return render(request,"lista_dosagem.html",context)

@login_required
def configura_horario_dosagem(request,id_receita):
    data_now = timezone.now()
    listHorarios = []
    
    objPessoa = Pessoa.objects.get(pk=request.user.id)
    primeiro_nome = objPessoa.nome_completo.split(None, 1)[0]
    objReceita = Receita.objects.get(pk=id_receita)

    try:
        objAgenda_receita = Agenda_receita.objects.get(receita=objReceita)
    except:
        objAgenda_receita = None

    totalDoze = int((objReceita.quantidade_dias*24)/objReceita.intervalo)
    if not objAgenda_receita:
        if request.POST:
            data_de_inicio = request.POST.get('data_de_inicio', None)  
            if data_de_inicio:       
                horario_inicio_remedio =datetime.datetime.strptime(data_de_inicio,'%Y-%m-%d %H:%M')    
                print(horario_inicio_remedio)
                objAgenda_receita = Agenda_receita()
                objAgenda_receita.receita = objReceita
                objAgenda_receita.data_inicio = horario_inicio_remedio 
                objAgenda_receita.data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)
                objAgenda_receita.save()
                
                objHorario = Horario_remedio()
                objHorario.agenda_receita = objAgenda_receita
                objHorario.horario = horario_inicio_remedio
                objHorario.save()
                
                for q in range(totalDoze):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_remedio()
                    objHorario.agenda_receita = objAgenda_receita
                    objHorario.horario = horario_inicio_remedio
                    objHorario.save()
                return redirect("dosagem_usuario",id_receita )  
            else:
                return redirect("configura_horario_dosagem",id_receita )
    else:

        listHorarios = Horario_remedio.objects.filter(agenda_receita=objAgenda_receita)

        totalDoze -= len(listHorarios)
        if request.POST:
            data_de_inicio = request.POST.get('data_de_inicio', None)
            if data_de_inicio:        
                horario_inicio_remedio =datetime.datetime.strptime(data_de_inicio,'%Y-%m-%d %H:%M')    
                print(horario_inicio_remedio)
                objAgenda_receita.reajuste = True
                objAgenda_receita.data_inicio = horario_inicio_remedio 
                objAgenda_receita.data_de_termino = horario_inicio_remedio + timezone.timedelta(days=objReceita.quantidade_dias)
                objAgenda_receita.save()
                
                objHorario = Horario_remedio()
                objHorario.agenda_receita = objAgenda_receita
                objHorario.horario = horario_inicio_remedio
                objHorario.save()
                
                for q in range(totalDoze):
                    horario_inicio_remedio += timezone.timedelta(hours=objReceita.intervalo)
                    objHorario = Horario_remedio()
                    objHorario.agenda_receita = objAgenda_receita
                    objHorario.horario = horario_inicio_remedio
                    objHorario.save()
                return redirect("dosagem_usuario",id_receita )
            else:
                return redirect("configura_horario_dosagem",id_receita )

    


    context = {
        "nome_pagina":"datas disponiveis",
        "usuario" : primeiro_nome,
        "listHorarios" : listHorarios,
    }

    return render(request,"configura_horarios.html",context)



