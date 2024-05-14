from django.urls import path, include
from .views import index, AlunoListCreate, getRoutes

urlpatterns = [
    path('alunos/', AlunoListCreate.as_view(), name='alunos-create-list'),
    path('', getRoutes, name='get-routes'),    
    
]
