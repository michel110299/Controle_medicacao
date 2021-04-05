from django import forms
from cadastro.models import *

class Remedioform(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ["nome_completo","descricao"]

class Pessoaform(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome_completo","cpf","data_nascimento","email"]

class Receitaform(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["pessoa","remedio","intervalo","data_inicio","dosagem"]