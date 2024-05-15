from .models import Aluno, Professor, Idioma, Curso, Disciplina, BoletimEscolar, Aula, FrequenciaEscolar, Matricula
from rest_framework import serializers
from django.urls import reverse


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

class AlunoDetail(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'email', 'telefone', 'idade']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

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