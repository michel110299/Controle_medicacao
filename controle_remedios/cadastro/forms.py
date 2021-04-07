from django import forms
from cadastro.models import *
from django.contrib.auth.models import User



class Remedioform(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ["nome_completo","descricao"]

class Pessoaform(forms.ModelForm):

    def save(self, commit=True):
        user = super(Pessoaform, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    class Meta:
        model = Pessoa
        fields = ["nome_completo","cpf","data_nascimento","email","password"]

class Receitaform(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["remedio","intervalo","data_inicio","quantidade_dias","dosagem"]