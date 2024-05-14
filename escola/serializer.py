from .models import Aluno, Professor, Idioma, Curso, Disciplina, BoletimEscolar, Aula, FrequenciaEscolar, Matricula
from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'
        
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = '__all__'
        
        
class DisciplinaSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Disciplina
        fields = '__all__'
        
        
class BoletimEscolarSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = BoletimEscolar
        fields = '__all__'
        
        

class AulaSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Aula
        fields = '__all__'
        
        

class FrequenciaEscolarSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = FrequenciaEscolar
        fields = '__all__'
        
        

class MatriculaSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Matricula
        fields = '__all__'