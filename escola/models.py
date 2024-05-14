from django.db import models
import random
import string
from datetime import date


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)  
    
    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25)    
    
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
    idiomas = models.ForeignKey(Idioma, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)  
    
    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25)    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'


class Curso(models.Model):

    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
        
    TURMA = (
        ('K', 'Kids'),
        ('T', 'Teens'),
        ('A', 'Adulto'),
        ('I', 'Idosos'),
    )
            
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)    
    codigo = models.CharField(max_length=8, unique=True, blank=True, editable=False)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    turma = models.CharField(max_length=1, choices=TURMA, blank=False, 
	    null=False)
    carga_horaria = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Curso  '
        verbose_name_plural = 'Cursos'
        
    def gerar_codigo_curso(self):
        if len(self.turma) >= 2:
            codigo = self.NIVEL[0][0] + self.turma[1]
        else:
            codigo = 'X' 
            codigo += ''.join(random.choices('0123456789', k=3))
        return codigo

    
    def save(self, *args, **kwargs):
        if not self.codigo:
            while True:
                codigo = self.gerar_codigo_curso()
                if not Curso.objects.filter(codigo=codigo).exists():
                    self.codigo = codigo
                    break
        super().save(*args, **kwargs)
        


class Matricula(models.Model):
    codigo = models.CharField(max_length=8, unique=True, editable=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.codigo)
    
    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        
    def gerar_codigo_matricula():
        letras = string.ascii_uppercase
        numeros = ''.join(random.choices(string.digits, k=4))
        codigo = ''.join(random.choices(letras, k=2)) + numeros
        return codigo
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            while True:
                codigo = self.gerar_codigo_matricula()
                if not Matricula.objects.filter(codigo=codigo).exists():
                    self.codigo = codigo
                    break
        super().save(*args, **kwargs)
    