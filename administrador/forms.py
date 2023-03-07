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

        widgets = {
            'produtos': forms.ModelMultipleChoiceField(
        queryset=produtos.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ),
            'instalador': forms.Select(attrs={ 'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data': forms.DateInput(attrs={ 'class': 'form-control','value':'date.today()','readonly':'readonly','id':'produtos'}),
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['produtos'].label_from_instance = lambda obj: obj.name
            self.fields['produtos'].widget.attrs['required'] = True
        def filter_queryset(self, queryset):
            search_term = self.cleaned_data.get('search')
            my_field = self.cleaned_data.get('produtos')
            if search_term:
                queryset = queryset.filter(name__icontains=search_term)
            if my_field:
                queryset = queryset.filter(my_field__in=my_field)
            return queryset