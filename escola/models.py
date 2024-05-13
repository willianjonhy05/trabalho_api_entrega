from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    data_nascimento = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
class Idioma(models.Model):
    codigo = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idioma'


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    data_nascimento = models.CharField(max_length=10)
    idiomas = models.ManyToManyField(Idioma, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
<<<<<<< HEAD
=======



>>>>>>> 74d9f260e55c5cbabb2a2587de4f0fb5d8014600
