from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
############# Rotas da Página Principal ######################
@api_view(["GET"])
def getRoutes(request):
    routes = {
    "Alunos": "http://127.0.0.1:8000/alunos/",
    "Idiomas": "http://127.0.0.1:8000/idioma/",
    "Professor": "http://127.0.0.1:8000/professor/",

}
    return Response(routes)

############# Views referente ao Aluno ######################

class AlunoListCreate(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoDetail

class MatriculasDoAluno(generics.ListAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
    def get_queryset(self):
        aluno_pk = self.kwargs['pk']
        aluno = Aluno.objects.get(id=aluno_pk)
        matriculas = Matricula.objects.filter(aluno=aluno)
        return matriculas

############# Views referente ao Professor ######################

class ProfessorListCreate(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorDetail

class IdiomaListCreate(generics.ListCreateAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class IdiomaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer


############# Views referente ao Aluno ######################