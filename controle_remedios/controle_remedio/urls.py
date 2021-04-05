from django.contrib import admin
from django.urls import path, include
from adm_remedio.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home" ),
    path('cadastro/',include('cadastro.urls')),
    path('adm/',include('adm_remedio.urls')),
]
