from django.urls import path, include
from .views import *

urlpatterns = [
    path('professor/detail/<int:pk>/', ProfessorRetrieveUpdateDestroy.as_view(), name='professor-detail'),
    path('professor/', ProfessorListCreate.as_view(), name='professor-create-list'),
    path('idioma/detail/<int:pk>/', IdiomaRetrieveUpdateDestroy.as_view(), name='idioma-detail'),
    path('idioma/', IdiomaListCreate.as_view(), name='idioma-create-list'),
    path('alunos/detail/<int:pk>/', AlunoRetrieveUpdateDestroy.as_view(), name='aluno-detail'),
    path('alunos/', AlunoListCreate.as_view(), name='alunos-create-list'),
    path('', getRoutes, name='get-routes'),    
    
]
