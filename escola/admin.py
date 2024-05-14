from django.contrib import admin
from .models import *


class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'rg', 'data_nascimento']
    
admin.site.register(Aluno, AlunoAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'rg', 'data_nascimento']
    
admin.site.register(Professor, ProfessorAdmin)


class IdiomaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome']
    

    
    
    
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(Disciplina)
admin.site.register(BoletimEscolar)
admin.site.register(Aula)
admin.site.register(FrequenciaEscolar)
admin.site.register(Matricula)
admin.site.register(Curso)