from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    
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
        verbose_name_plural = 'Idiomas'


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    idiomas = models.ForeignKey(Idioma, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'