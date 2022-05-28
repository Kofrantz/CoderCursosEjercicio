from django.shortcuts import render
from .models import Curso, Estudiante

# Create your views here.
def cursos(request):
    cursos_list = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos_list})

def students(request, id):
    estudiantes = Estudiante.objects.filter(curso=id)
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})
