from django.db import models


class Pessoa(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name= "CPF",
        max_length = 14,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length = 194,
        unique = True,
        null = True,
        blank = True,
    )
    horario_criacao = models.DateTimeField(
        verbose_name= "Horário de criação",
        auto_now_add = True,
        null = True,
        blank = True,
    )
    class Meta:
        verbose_name = "Pessoa"
        db_table = "pessoa"

    def __str__(self):
        return self.nome_completo

class Remedio(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )
    descricao = models.TextField(
        verbose_name = "Descricao",
        max_length = 350,
    )
    class Meta:
        verbose_name = "Remedio"
        verbose_name_plural = "Remedios"
        db_table = "remedio"

    def __str__(self):
        return self.nome_completo


class Receita(models.Model):

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete = models.CASCADE,
        verbose_name = "Nome do paciente",
    )
    remedio = models.ForeignKey(
        Remedio,
        on_delete = models.CASCADE,
        verbose_name = "Nome do remedio",
    )
    intervalo = models.FloatField(
        verbose_name = "Intervalo de tempo",
        default = 0,
    )
    data_inicio = models.DateField(
        verbose_name="Data de inicio para tomar o remédio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    dosagem = models.FloatField(
        verbose_name = "Dosagem do Remédio",
        default = 0,
    )