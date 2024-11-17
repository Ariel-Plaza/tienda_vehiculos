
from django import forms
from .models import Vehiculos

class VehiculosForm(forms.ModelForm):
  # fecha_creacion = forms.DateTimeField(widget=forms.DateTimeInput(
  #     attrs={'type': 'datetime-local'}), input_formats=['%d-%m-%YT%H:%M'])
  # fecha_modificacion = forms.DateTimeField(widget=forms.DateTimeInput(
  #     attrs={'type': 'datetime-local'}), input_formats=['%d-%m-%YT%H:%M'])

  class Meta:
    model = Vehiculos
    # campos que tiene el modelo
    fields = ['marca', 'modelo', 'serial_carroceria',
              'serial_motor', 'categoria', 'precio']
