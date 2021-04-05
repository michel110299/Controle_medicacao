from django.urls import path
from .import views

urlpatterns = [
    path('registrar-remedio/', views.registrar_remedio, name="registrar_remedio"),
    path('registrar-pessoa/', views.registrar_pessoa, name="registrar_pessoa"),
    path('registrar-receita/', views.registrar_receita, name="registrar_receita"),
    path('login-usuario/', views.login_usuario, name="login_usuario"),
]