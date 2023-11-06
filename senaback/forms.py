from django import forms
from .models import ElementoConsumible
from .models import ElementoDevolutivo
from .models import entrega

class FiltroElementoForm(forms.Form):
    nombre_consumible = forms.CharField(max_length=100, required=False)
    categoria = forms.CharField(max_length=50, required=False)
    serial = forms.CharField(max_length=20, required=False)
    nombre_devolutivo = forms.CharField(max_length=100, required=False)
    categoria_devolutivo = forms.CharField(max_length=50, required=False)
    serial_devolitivo = forms.CharField(max_length=20, required=False)
    

class ElementoConsumibleForm (forms.ModelForm):
    class Meta:
        model = ElementoConsumible
        fields = '__all__' 
        
class ElementoDevolutivoForm (forms.ModelForm):
    class Meta:
        model = ElementoDevolutivo
        fields = '__all__' 

class EntregaForm(forms.ModelForm):
    class Meta:
        model = entrega
        fields = ['elemento_entrega', 'cantidad', 'responsable_entrega', 'observaciones']
