from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):

    def create_user(self,cpf,password=None):
        usuario = self.model(
            cpf = cpf
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()
        
        return usuario
    
    def create_superuser(self,cpf,password):
        usuario = self.create_user(

            cpf = cpf,
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario
 

class Pessoa(AbstractBaseUser,PermissionsMixin):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
        null = True,
        blank = True,
    )

    cpf = models.CharField(
        verbose_name= "CPF",
        max_length = 14,
        unique = True
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
        null = True,
        blank = True,
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

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True, 
    )
    is_staff  = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default= False,
    )

    is_superuser = models.BooleanField(
        verbose_name= "Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "cpf"

    objects = UsuarioManager()

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
    quantidade_dias = models.IntegerField(
        verbose_name = "Total de dias",
        help_text = "total de dias que será consumido o remédio",
        default = 0,
    )
    intervalo = models.FloatField(
        verbose_name = "Intervalo de tempo em horas",
        blank = False,
        null = False,
    )
    data_inicio = models.DateField(
        verbose_name="Data de inicio para tomar o remédio",
        auto_now= False,
        blank = True, 
        null = True,
    )
    dosagem = models.FloatField(
        verbose_name = "Dosagem do Remédio",
        blank = False,
        null = False,
    )
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        db_table = "receita"

    def __str__(self):
        return "%s - %s" % (self.remedio.nome_completo, self.pessoa.nome_completo)