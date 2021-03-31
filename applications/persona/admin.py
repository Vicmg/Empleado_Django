from django.contrib import admin
from .models import Persona,Habilidades
# Register your models here.

admin.site.register(Persona)


#decoradores

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'habilidades',
        'job'
    )

admin.site.register(Habilidades, EmpleadoAdmin)