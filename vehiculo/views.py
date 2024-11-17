from django.shortcuts import render
from .forms import VehiculosForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import Vehiculos
from django.contrib import messages



# Create your views here.

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El vehiculo ha sido agregado con éxito')
            return redirect('vehiculo:agregar_vehiculo')
    else:
        form = VehiculosForm()
    return render(request, 'vehiculo/agregar.html', {'form': form})