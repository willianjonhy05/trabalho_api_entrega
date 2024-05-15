from .models import *
from rest_framework import serializers
from django.urls import reverse
from .models import Matricula

############# Serializers referente ao Aluno ######################
class AlunoSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'telefone', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('aluno-detail', kwargs={'pk': obj.pk}))
        return None

class CriarAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class AlunoDetail(serializers.ModelSerializer):
    matriculas = serializers.SerializerMethodField()
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'email', 'telefone', 'idade', 'matriculas']
        
    def get_matriculas(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('matriculas-do-aluno', kwargs={'pk': obj.pk}))
        return None


############# Serializers referente ao Professor ######################

class ProfessorSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    disciplinas = serializers.SerializerMethodField()
    class Meta:        
        model = Professor
        fields = ['nome', 'email', 'telefone', 'link']
        
    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('professor-detail', kwargs={'pk': obj.pk}))
        return None
    
    def get_disciplinas(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('professor-disciplinas', kwargs={'pk': obj.pk}))
        return None
    
class ProfessorDetail(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'email', 'telefone', 'idade', 'idiomas']
        
class CriarProfessor(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        
############# Serializers referente ao Idioma ######################
        
class IdiomaSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Idioma
        fields = '__all__'

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('idioma-detail', kwargs={'pk': obj.pk}))
        return None
    
############################ Serializers do Curso ################################
        
class CursoSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    idioma = serializers.ReadOnlyField(source='idioma.nome')
    class Meta:
        model = Curso
        fields = ['codigo', 'idioma', 'nome', 'carga_horaria', 'link']
        
    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('cursos-detail', kwargs={'pk': obj.pk}))
        return None
        
class CriarCurso(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class CursoDetail(serializers.ModelSerializer):
    nome_turma = serializers.SerializerMethodField()
    nivel_turma = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['idioma', 'codigo', 'nome_turma', 'descricao', 'nivel_turma', 'carga_horaria']

    def get_nome_turma(self, obj):
        return dict(Curso.TURMA)[obj.turma]

    def get_nivel_turma(self, obj):
        return dict(Curso.NIVEL)[obj.nivel]


############################ Serializers da Matrícula ################################### 

class ListaMatriculas(serializers.ModelSerializer): 
    aluno = serializers.ReadOnlyField(source='aluno.nome')   
    curso = serializers.ReadOnlyField(source='curso.nome')
    link = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['codigo', 'aluno', 'curso', 'status', 'link']
        
    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-matriculas', kwargs={'pk': obj.pk}))
        return None


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula        
        fields = ['codigo', 'aluno', 'curso', 'status']

      
############################ Serializers do Aula ###################################  

class AulaSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    disciplina = serializers.ReadOnlyField(source='disciplina.nome')
    
    class Meta:
        model = Aula
        fields = ['disciplina', 'data', 'link']
        
    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-aulas', kwargs={'pk': obj.pk}))
        return None
              
class AulaSerializerDois(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ['disciplina', 'data', 'sala', 'observacoes']
           

############################ Serializers da Disciplina ################################

class DisciplinaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Disciplina
        fields = '__all__'


class DisciplinaList(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    curso = serializers.ReadOnlyField(source='curso.nome')
    
    class Meta:
        model = Disciplina
        fields = ['nome', 'curso', 'link']
        
    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-disciplina', kwargs={'pk': obj.pk}))
        return None

############################ Serializers do Boletim ################################### 

class BoletimEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletimEscolar
        fields = '__all__'



############################ Serializers do Frequência################################### 
        

class FrequenciaEscolarSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = FrequenciaEscolar
        fields = '__all__'
        
