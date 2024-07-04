from django.db import models
from django.conf import Settings

class curso(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nombre = models.CharField(max_length=40)
    division = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return f"curso:{self.nombre} | division:{self.division}"



class mate(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nombre = models.CharField(max_length=30)
    codigo= models.IntegerField()
    profesor = models.CharField(max_length=30)
    profesor = models.ForeignKey('prof',null=True, on_delete= models.CASCADE)
    
    class Meta:
        db_table = 'Materias'
    

    def __str__(self):
        return f"Nombre de Materia: {self.nombre} Codigo: {self.codigo} Profesor: {self.profesor}"
    
class CursoMateria(models.Model):

    id = models.AutoField(primary_key=True, db_column='ID')
    cursos = models.ForeignKey(curso,null=True, on_delete= models.CASCADE)
    materia = models.ForeignKey(mate,null=True, on_delete= models.CASCADE)

    class Meta:
        db_table = 'CursoMateria'

    def __str__(self):
        return f"Nombre de curso: {self.cursos} materia: {self.materia}"




class estu(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni= models.IntegerField()
    email = models.EmailField(max_length=40)

    class Meta:
        db_table = 'Estudiantes'
        
    def __str__(self):
        return f"nombre:{self.nombre} | apellido:{self.apellido} | dni:{self.dni} "

class alum(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni= models.IntegerField()
    email = models.EmailField(max_length=40)

    class Meta:
        db_table = 'Alumnos'

    def __str__(self):
        return f"nombre:{self.nombre} | apellido:{self.apellido} | dni:{self.dni} "

class prof(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni= models.IntegerField()
    email = models.EmailField(max_length=40)
    

    class Meta:
        db_table = 'Profesores'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"     