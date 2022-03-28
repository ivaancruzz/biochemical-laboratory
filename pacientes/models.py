from django.db import models


# Create your models here.
class Paciente( models.Model ):
    nombre = models.CharField( max_length=200 )
    apellido = models.CharField( max_length=200 )
    dni = models.CharField( max_length= 10, primary_key=True )
    celular = models.CharField( max_length=200 )
    direccion = models.CharField( max_length= 200 )
    fecha_registro = models.DateTimeField( auto_now_add=True)

    
    SEX_CHOICE = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('I', 'Indefinido',),
    )

    sexo = models.CharField(
        max_length= 1,
        choices=SEX_CHOICE,
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'