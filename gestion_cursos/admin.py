from django.contrib import admin
from .models import Categoria,Curso,Proyecto, Inscripcion

admin.site.register(Categoria)
admin.site.register(Curso)
admin.site.register(Proyecto)
admin.site.register(Inscripcion)
