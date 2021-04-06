from django.contrib import admin
from django.urls import path, include
from adm_remedio.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LoginView.as_view(template_name='login_usuario.html'), name='login'),
    path('cadastro/',include('cadastro.urls')),
    path('adm/',include('adm_remedio.urls')),
]
