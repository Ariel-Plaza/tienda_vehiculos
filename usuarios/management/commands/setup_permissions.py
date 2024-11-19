from django.contrib.auth.models import User, Group,Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Configuracion de permiso visualizar catalago'
    
    def handle(self, *args, **kwargs):
        
        grupos_permisos = {'Editor':['view_vehiculos', 'add_vehiculos'],
                            'Usuario':['view_vehiculos'],}
            
        for grupo_nombre, permisos in grupos_permisos.items():
                grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
                    
                for permisos_codename in permisos:
                        permiso = Permission.objects.get(codename=permisos_codename)
                        grupo.permissions.add(permiso)
        
        if creado:
            self.stdout.write(self.style.SUCCESS(f"Grupo creado y permisos asignados con exito"))
        
        else:
            self.stdout.write(self.style.WARNING(
                f"Grupo ya existe"))
