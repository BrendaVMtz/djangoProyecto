from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class usuario(AbstractUser):
    numero_de_telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Tarea(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(validators=[MinValueValidator(12), MaxValueValidator(100)])
    identificacion = models.FileField(upload_to='users/', default='default.pdf')
    diagnostico = models.FileField(upload_to='users/', default='default.pdf')

    def __str__(self):
        return self.nombre

DELEGACIONES_CDMX = [
    ('ALVARO', 'Álvaro Obregón'),
    ('AZCAPOTZALCO', 'Azcapotzalco'),
    ('BENITO', 'Benito Juárez'),
    ('COYOACAN', 'Coyoacán'),
    ('CUAJIMALPA', 'Cuajimalpa de Morelos'),
    ('CUAUHTEMOC', 'Cuauhtémoc'),
    ('GUSTAVO', 'Gustavo A. Madero'),
    ('IZTACALCO', 'Iztacalco'),
    ('IZTAPALAPA', 'Iztapalapa'),
    ('MAGDALENA', 'La Magdalena Contreras'),
    ('MIGUEL', 'Miguel Hidalgo'),
    ('MILPA', 'Milpa Alta'),
    ('TLAHUAC', 'Tláhuac'),
    ('TLALPAN', 'Tlalpan'),
    ('VENUSTIANO', 'Venustiano Carranza'),
    ('XOCHIMILCO', 'Xochimilco'),
]

class Profesor(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    institucion = models.CharField(max_length=100)
    titulo_academico = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100, choices=DELEGACIONES_CDMX)

    def __str__(self):
        return 'Profesor: ' + self.usuario.username

class Padre(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100, choices=DELEGACIONES_CDMX)
    codigo_postal = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Padre: ' + self.usuario.username

class Salud(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    institucion = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100, choices=DELEGACIONES_CDMX)

    def __str__(self):
        return 'Profesional-salud: ' + self.usuario.username

     