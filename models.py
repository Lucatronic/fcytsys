# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    id = models.IntegerField(primary_key=True)
    carrera = models.CharField(max_length=23)
    ingreso = models.IntegerField()
    codigo = models.IntegerField()
    apellidos = models.CharField(max_length=21)
    nombre = models.CharField(max_length=22)
    ci = models.IntegerField()
    institucion = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='institucion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno'


class Institucion(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_departamento = models.IntegerField()
    nombre_departamento = models.CharField(max_length=19)
    codigo_distrito = models.IntegerField()
    nombre_distrito = models.CharField(max_length=31)
    codigo_barrio_localidad = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    nombre_barrio_localidad = models.CharField(max_length=43, blank=True, null=True)
    codigo_zona = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    nombre_zona = models.CharField(max_length=6, blank=True, null=True)
    codigo_establecimiento = models.CharField(max_length=7)
    codigo_institucion = models.CharField(max_length=7)
    nombre_institucion = models.CharField(max_length=99)
    sector_o_tipo_gestion = models.CharField(max_length=21, blank=True, null=True)
    niveles_modalidades = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'institucion'
