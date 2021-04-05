from django.db import models
from cadastro.models import *

class Agenda_receita(models.Model):
    receita = models.ForeignKey(
        Receita,
        on_delete = models.CASCADE,
        verbose_name = "Receita",
    )
    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )
    data_inicio = models.DateTimeField(
        verbose_name="Data de inicio para tomar o remédio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    data_termino = models.DateTimeField(
        verbose_name="Data do termino para tomar o remédio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    concluido = models.BooleanField(
        verbose_name = "Concluido",
        default = False,
    )
    reajuste = models.BooleanField(
        verbose_name = "Reajuste",
        default = False,
    )
    class Meta:
        verbose_name = "Agenda da receita"
        verbose_name_plural = "Agenda das receitas"
        db_table = "agenda_receita"

    def __str__(self):
        return self.receita

class Horario_remedio(models.Model):
    agenda_receita = models.ForeignKey(
        Agenda_receita,
        on_delete = models.CASCADE,
        verbose_name = "Receita",
    )
    horario = models.DateTimeField(
        verbose_name="Horario para tomar remédio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    concluido = models.BooleanField(
        verbose_name = "Concluido",
        default = False,
    )
    class Meta:
        verbose_name = "Horário do remédio"
        verbose_name_plural = "Horários do remédio"
        db_table = "horário_remedio"

    def __str__(self):
        return self.agenda_receita




