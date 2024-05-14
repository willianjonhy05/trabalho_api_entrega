import os
import django
from django.db import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trabalho.settings')
django.setup()
from escola.models import Curso, Idioma
import random

def gerar_cursos():
    idiomas = Idioma.objects.all()
    niveis = ['Básico', 'Intermediário', 'Avançado']
    turmas = ['Kids', 'Teens', 'Adulto', 'Idosos']
    carga_horaria = [20, 30, 40, 50, 60]
    descricao = "Descrição do curso..."
    
    cursos_gerados = []
    
    for _ in range(10):
        idioma = random.choice(idiomas)
        nivel = random.choice(niveis)
        turma = random.choice(turmas)
        carga = random.choice(carga_horaria)
        nome = f"{idioma.nome} {nivel} - {turma}"
        
        while True:
            try:
                curso = Curso.objects.create(
                    idioma=idioma,
                    nome=nome,
                    descricao=descricao,
                    turma=turma[0],
                    carga_horaria=carga
                )
                curso.codigo = curso.gerar_codigo_curso()
                curso.save()
                cursos_gerados.append(curso)
                break  
            except IntegrityError:
                continue  
        
    return cursos_gerados


gerar_cursos()
