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
    nivel = models.CharField(max_length=1, default='A', choices=NIVEL, blank=False, 
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
        

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ementa = models.TextField("Ementa da Disciplina")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
    
class BoletimEscolar(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota_um = models.DecimalField("Nota 1", blank=True, null=True, max_digits=5, decimal_places=2)
    nota_dois = models.DecimalField("Nota 2", blank=True, null=True, max_digits=5, decimal_places=2)
    nota_tres = models.DecimalField("Nota 3", blank=True, null=True, max_digits=5, decimal_places=2)
    nota_quatro = models.DecimalField("Nota 4", blank=True, null=True, max_digits=5, decimal_places=2)
    
    @property
    def media(self):
        notas = [self.nota_um, self.nota_dois, self.nota_tres, self.nota_quatro]
        if notas:
            zeros = notas.count(0)
            nao_zeros = len(notas) - zeros
            total = sum(notas)
            media = total / nao_zeros
            return "{:.2f}".format(media) 
        else:
            return None
    
    def __str__(self):
        return f'Boletim do {self.aluno.nome}'
    
    class Meta:
        verbose_name = 'BoletimEscolar'
        verbose_name_plural = 'Boletins Escolares'
            

class Aula(models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    data = models.DateField("Data da Aula")
    sala = models.CharField(max_length=5, verbose_name="Sala de Aula")
    
    def __str__(self):
        return self.disciplina
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

class FrequenciaEscolar(models.Model):
    aula = models.OneToOneField(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    presenca = models.BooleanField(default=True)
    
    def __str__(self):
        return self.aula

    class Meta:
        verbose_name = 'Frequencia Escolar'
        verbose_name_plural = 'Frequencias Escolares'


class Matricula(models.Model):
    STATUS = (
        ('I', 'Ativa - Iniciando'),
        ('A', 'Ativa - Em andamento'),
        ('C', 'Desativada - Concluída'),
        ('S', 'Desativada - Suspensa'),
    )
    
    
    codigo = models.CharField(max_length=8, unique=True, editable=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    boletim = models.OneToOneField(BoletimEscolar, on_delete=models.CASCADE, blank=True, null=True)
    frequencia = models.OneToOneField(FrequenciaEscolar, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='I', blank=False, 
	    null=False)
    
    def __str__(self):
        return self.aluno
    
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
    
    
