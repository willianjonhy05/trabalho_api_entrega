from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Matricula, BoletimEscolar, FrequenciaEscolar

# @receiver(post_save, sender=Matricula)
# def criar_matricula(sender, instance, created, **kwargs):
#     if created:
#         boletim_escolar = BoletimEscolar.objects.create(aluno=instance.aluno)
#         frequencia_escolar = FrequenciaEscolar.objects.create(aluno=instance.aluno)
#         instance.boletim = boletim_escolar
#         instance.frequencia = frequencia_escolar
#         instance.save()
    
