from django.shortcuts import render
from rest_framework import generics
from .models import Aluno
from .serializer import AlunoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, 'home.html')

@api_view(["GET"])
def getRoutes(request):
    routes = {
    "Alunos": "http://127.0.0.1:8000/alunos/",

}
    return Response(routes)


class AlunoListCreate(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
