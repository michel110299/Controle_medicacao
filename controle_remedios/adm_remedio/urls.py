from django.urls import path
from .import views

urlpatterns = [
    path('dashbord-usuario/', views.dashbord_usuario, name="dashboard_usuario"),
    path('dosagens-usuario/', views.dosagem_usuario, name="dosagem_usuario"),
    ]