from django import forms
from datetime import date
from administrador.models import vendas
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from searchableselect.widgets import SearchableSelect

class VendaForm(forms.ModelForm):

    class Meta:
        model = vendas
        fields = ('produtos','instalador','quantidade','data')

        widgets = {
            'produtos': SearchableSelect(model='falcao.produtos', search_field='nome', limit=10),
            'instalador': forms.Select(attrs={ 'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data': forms.DateInput(attrs={ 'class': 'form-control','value':'date.today()','readonly':'readonly','id':'produtos'}),
            
        }