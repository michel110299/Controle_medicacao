from django.shortcuts import render



def home(request):
    
    context = {
        "nome_pagina":"home",
    }

    return render(request,"home.html",context)


def dashbord_usuario(request):
    
    context = {
        "nome_pagina":"Dashboard",
    }

    return render(request,"dashboard_usuario.html",context)
def dosagem_usuario(request):
    
    context = {
        "nome_pagina":"Dosagens",
    }

    return render(request,"lista_dosagem.html",context)

