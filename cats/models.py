from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=64, verbose_name='Raza')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'


class Cat(models.Model):
    # Animal Gender
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = (
        (FEMALE, 'Hembra'),
        (MALE, 'Macho'),
    )

    # Animal Hair
    SHORT = 'S'
    MEDIUM = 'M'
    LONG = 'L'
    HAIR_CHOICES = (
        (SHORT, 'Corto'),
        (MEDIUM, 'Semi-Largo'),
        (LONG, 'Largo'),
    )

    name = models.CharField(max_length=64, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Nacimiento',null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, verbose_name='Sexo', blank=True)
    breed = models.ForeignKey(Breed, related_name='animals', verbose_name='Raza')
    color = models.CharField(max_length=32, verbose_name='Color de pelo', null=True, blank=True)
    hair = models.CharField(max_length=1, choices=HAIR_CHOICES, verbose_name='Longitud de pelo', null=True, blank=True)
    image = models.ImageField(upload_to='animals', verbose_name='Foto', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Gato'
        verbose_name_plural = 'Gatos'