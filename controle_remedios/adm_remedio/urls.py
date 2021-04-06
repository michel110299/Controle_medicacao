from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('dashbord-usuario/', views.dashbord_usuario, name="dashboard_usuario"),
    path('dosagens-usuario/<int:id_receita>/', views.dosagem_usuario, name="dosagem_usuario"),
    path('configurar-horarios-dosagens/', views.configura_horario_dosagem, name="configura_horario_dosagem"),
    ]
