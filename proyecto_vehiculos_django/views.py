from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')


def custom_403_view(request, exception): 
    context = { 
                "message": "No tienes permiso para acceder a esta página." 
            } 
    return render(request, "403.html", context)