from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('professor/', ProfessorListCreate.as_view(), name='professor-create-list'),
    path('professor/detail/<int:pk>/', ProfessorRetrieveUpdateDestroy.as_view(), name='professor-detail'),
    
    path('cursos/', CursoListCreate.as_view(), name='cursos'),
    path('cursos/detail/<int:pk>/', CursoRetrieveUpdateDestroy.as_view(), name='cursos-detail'),
    
    path('idioma/', IdiomaListCreate.as_view(), name='idioma-create-list'),
    path('idioma/detail/<int:pk>/', IdiomaRetrieveUpdateDestroy.as_view(), name='idioma-detail'),
    
    path('alunos/', AlunoListCreate.as_view(), name='alunos-create-list'),
    path('alunos/detail/<int:pk>/', AlunoRetrieveUpdateDestroy.as_view(), name='aluno-detail'),
    path('matriculas/alunos/detail/<int:pk>/', MatriculasDoAluno.as_view(), name='matriculas-do-aluno'),
    
    path('matriculas/', ListaMatriculasView.as_view({'get': 'list'}), name='lista-matriculas'),
    path('matriculas/nova/', CriarMatricula.as_view(), name='nova-matricula'),
    path('matriculas/detail/<int:pk>/', MatriculaRetrieveUpdateDestroy.as_view(), name='detail-matriculas'),
    
    path('aulas/', ListaAulasView.as_view({'get': 'list'}), name='lista-aulas'),
    path('aulas/nova/', CriarAula.as_view(), name='nova-aula'),
    path('aulas/detail/<int:pk>/', AulaRetrieveUpdateDestroy.as_view(), name='detail-aulas'),
    
    path('disciplina/nova/', NovaDisciplina.as_view(), name='nova-disciplina'),
    path('disciplinas/todas/', ListarDisciplinas.as_view({'get': 'list'}), name='lista-disciplina'),
    path('disciplinas/detail/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view(), name='detail-disciplina'),
    
    
    
]
