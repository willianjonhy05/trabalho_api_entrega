from django.contrib import admin
from .models import Professor, Aluno, Idioma


class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'rg', 'data_nascimento']
    
admin.site.register(Aluno, AlunoAdmin)