from django.db import models
import uuid

# Create your models here.
class Curso(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=100)
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()

class Estudiante(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=100)
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)

