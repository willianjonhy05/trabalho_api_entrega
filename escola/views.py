from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
############# Rotas da Página Principal ######################
@api_view(["GET"])
def getRoutes(request):
    routes = {
    "Alunos": "http://127.0.0.1:8000/alunos/",
    "Idiomas": "http://127.0.0.1:8000/idioma/",
    "Professor": "http://127.0.0.1:8000/professor/",
    "Cursos": "http://127.0.0.1:8000/cursos/",
    "Matrículas": "http://127.0.0.1:8000/matriculas/",
    "Nova Matrícula": "http://127.0.0.1:8000/matriculas/nova/",
    "Aulas": "http://127.0.0.1:8000/aulas/",
    "Cadastrar Aula": "http://127.0.0.1:8000/aulas/nova/",
    "Disciplinas": "http://127.0.0.1:8000/disciplina/todas/",
    "Cadastrar Disciplina": "http://127.0.0.1:8000/disciplina/nova/",
    "Listar/Cadastrar Boletim": "http://127.0.0.1:8000/boletim/",
    "Listar/Cadastrar Frequência": "http://127.0.0.1:8000/frequencia/",


}
    return Response(routes)

############# Views referente ao Aluno ######################

class AlunoListCreate(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.method == 'POST': 
            return CriarAlunoSerializer
        return self.serializer_class

class AlunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoDetail

class MatriculasDoAluno(generics.ListAPIView):
    queryset = Matricula.objects.all()
    serializer_class = ListaMatriculas
    
    def get_queryset(self):
        aluno_pk = self.kwargs['pk']
        aluno = Aluno.objects.get(id=aluno_pk)
        matriculas = Matricula.objects.filter(aluno=aluno)
        return matriculas

############# Views referente ao Professor ######################

class ProfessorListCreate(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.method == 'POST': 
            return CriarProfessor
        return self.serializer_class

class ProfessorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorDetail


############# Views referente ao Idioma ######################

class IdiomaListCreate(generics.ListCreateAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome',]

class IdiomaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer


############# Views referente ao Curso ######################

class CursoListCreate(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome', 'codigo']
    filterset_fields = ['nivel', 'turma', 'idioma']
    
    def get_serializer_class(self):
        if self.request.method == 'POST': 
            return CriarCurso
        return self.serializer_class
    
class CursoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoDetail
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']: 
            return CriarCurso
        return self.serializer_class
    
############# Views referente a Matrícula ######################

class ListaMatriculasView(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = ListaMatriculas
    
class CriarMatricula(generics.CreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)        
        return redirect('lista-matriculas')
    
class MatriculaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
############# Views referente a Aulas ######################

class ListaAulasView(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializerDois
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome', ]
    
    
class CriarAula(generics.CreateAPIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializerDois

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)        
        return redirect('lista-aulas')
    
class AulaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializerDois
    
############# Views referente a Disciplina ######################

class ListarDisciplinas(viewsets.ModelViewSet):
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome', ]

class NovaDisciplina(generics.CreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)        
        return redirect('lista-disciplina')
    
class DisciplinaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = AulaSerializerDois

class DisciplinaPorProfessor(generics.ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaList
    
    def get_queryset(self):
        professor_pk = self.kwargs['pk']
        profs = Professor.objects.get(id=professor_pk)
        disciplinas = Disciplina.objects.filter(professor=profs)        
        return disciplinas

############# Views referente a Boletim ######################

class BoletimEscolarListCreate(generics.ListCreateAPIView):
    queryset = BoletimEscolar.objects.all()
    serializer_class = BoletimEscolarSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # ordering_fields = ['nome', ]
    # search_fields = ['nome',]

class BoletimEscolarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoletimEscolar.objects.all()
    serializer_class = BoletimEscolarSerializer


############# Views referente a Frequencia ######################

class FrequenciaEscolarListCreate(generics.ListCreateAPIView):
    queryset = FrequenciaEscolar.objects.all()
    serializer_class = FrequenciaEscolarSerilizer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # ordering_fields = ['nome', ]
    # search_fields = ['nome',]

class FrequenciaEscolarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrequenciaEscolar.objects.all()
    serializer_class = FrequenciaEscolarSerilizer

