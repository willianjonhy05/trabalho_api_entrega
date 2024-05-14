import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trabalho.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from escola.models import Aluno, Professor, Idioma

def criando_alunos(quantidade_de_pessoas):
    Faker.seed(5) 
    fake = Faker('pt_BR')  
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()        
       
        rg = "{:02d}{:03d}{:03d}{:01d}".format(random.randint(10, 99), random.randint(100, 999), random.randint(100, 999), random.randint(0, 9))
        telefone = "{} 9{}-{}".format(random.randint(10, 20), random.randint(4000, 9999), random.randint(4000, 9999))
        p = Aluno(nome=nome, data_nascimento=data_nascimento, rg=rg, cpf=cpf, email=email, telefone=telefone)
        p.save()

criando_alunos(100)
print("Alunos criados com Sucesso!")


def criando_professores(quantidade_de_professores):
    Faker.seed(5) 
    fake = Faker('pt_BR')  
    for _ in range(quantidade_de_professores):
        cpf = CPF()
        nome = fake.name()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '') 
        cpf = cpf.generate()        
        
        rg = "{:02d}{:03d}{:03d}{:01d}".format(random.randint(10, 99), random.randint(100, 999), random.randint(100, 999), random.randint(0, 9))
        telefone = "{} 9{}-{}".format(random.randint(10, 20), random.randint(4000, 9999), random.randint(4000, 9999))
        p = Professor(nome=nome, data_nascimento=data_nascimento, rg=rg, cpf=cpf, email=email, telefone=telefone)
        p.save()

criando_professores(100)
print("Professores criados com Sucesso!")

def gerar_idiomas():
    idiomas = [
        ('Inglês', 'ENG'),
        ('Espanhol', 'ESP'),
        ('Francês', 'FRA'),
        ('Italiano', 'ITA'),
        ('Alemão', 'DEU')
    ]
    
    for nome, codigo in idiomas:
        Idioma.objects.get_or_create(nome=nome, codigo=codigo)


gerar_idiomas()
print("Idiomas criados com Sucesso!")
print("Fim!")