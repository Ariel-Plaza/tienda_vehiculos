from .forms import VehiculosForm
from django.shortcuts import render, redirect
from .models import Vehiculos
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied



# Create your views here.
@login_required()
@permission_required('vehiculo.add_vehiculos', raise_exception=True)
def agregar_vehiculo(request): 
    if request.method == 'POST': 
        form = VehiculosForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'El vehículo ha sido agregado con éxito') 
            return redirect('vehiculo:agregar_vehiculo') 
    else: 
        form = VehiculosForm() 
    return render(request, 'vehiculo/agregar.html', {'form': form})

@login_required()
@permission_required('vehiculo.view_vehiculos', raise_exception=True)
def listar(request):
    vehiculos = []
    try: 
        # bajo,  entre  0  y  10000
        # vehiculos = Vehiculos.objects.filter(precio_alto = precio)
        vehiculos = Vehiculos.objects.all()
        # vehiculos = Vehiculos
        if not vehiculos:
            raise ValueError("No hay vehiculos en este momento.")
    except Exception as e:
        return render(request, 'vehiculo/listar.html'),{'error': 'Se produjo un error inesperado.'}
    context={
        # 'todos_los_vehiculos':vehicul,
        'vehiculos': vehiculos
    }
    
    return render(request, 'vehiculo/listar.html', context)
