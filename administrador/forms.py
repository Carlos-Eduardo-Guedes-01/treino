from django import forms
from datetime import date
from administrador.models import vendas
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from falcao.models import *
from django_select2.forms import Select2Widget

class VendaForm(forms.ModelForm):

    
    class Meta():
        model = vendas
        fields = ('produtos','instalador','quantidade','data')
        hj=date.today()
        widgets = {
            'produtos': forms.Select(attrs={ 'class': 'form-control', 'id':'id_product'}),
            'instalador': forms.Select(attrs={ 'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data': forms.DateInput(attrs={ 'class': 'form-control','value':hj,'readonly':'readonly'}),
            'preco':forms.TextInput(attrs={'class':'form-control','id':'id_price'}),
        }