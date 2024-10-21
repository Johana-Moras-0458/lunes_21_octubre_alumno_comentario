from django.contrib import admin
from .models import Alumno, Frase
# Register your models here.

class ComentarioInnLine(admin.TabularInline): #agregan comentarios
    model=Frase
    extra=1


class AlumnoAdmin(admin.ModelAdmin):
    fields=["apatarno","amaterno","nombre","fecha_nacimiento","fecha_ingreso"]
    list_display=["apatarno","amaterno","nombre"]
    inlines=[ComentarioInnLine]

admin.site.register(Alumno,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
        fields=["comentario","Alumno_fk"]
        list_display=["comentario"]