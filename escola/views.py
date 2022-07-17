# Esse arquivo converte os dados para o python nativo
# Buscando os dados que estão na base de dados

from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Exibindo todas as matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

