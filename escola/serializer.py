from .models import Aluno, Curso, Idioma
from rest_framework import serializers


class Aluno(serializers.ModelSerializer):
    ...