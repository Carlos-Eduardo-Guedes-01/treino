from django import forms
from datetime import date
from administrador.models import vendas

class LivroForm(forms.ModelForm):

    class Meta:
        model = vendas
        fields = ('produtos','instalador','quantidade','data')

        widgets = {
            'produtos': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'instalador': forms.Select(attrs={ 'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data': forms.DateInput(attrs={ 'class': 'form-control','value':'date.today()','readonly':'readonly'}),
        }