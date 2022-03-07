from dataclasses import fields
from django.forms import ModelForm
from app.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','sobrenome','produto','valor']