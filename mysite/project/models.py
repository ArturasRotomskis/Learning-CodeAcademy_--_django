from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Projektas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    vadovas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    darbuotojai = models. ForeignKey("Darbuotojas", on_delete=models.SET_NULL, null=True, blank=True)
    darbai = models.ForeignKey("Darbas", on_delete=models.SET_NULL, null=True, blank=True)
    saskaitos = models.ForeignKey("Saskaita", on_delete=models.SET_NULL, null=True, blank=True)
    klientas = models.ManyToManyField("Klientas")
    start_time = models.DateField("Pradžios laikas")
    end_time = models.DateField("Pabaigos laikas")


class ProjektoAprasymas(models.Model):
    tekstas = HTMLField("Projekto aprašymas")


    class Meta:
        verbose_name = "Projekto aprašymas"
        verbose_name_plural = "Projekto aprašymas"


class Klientas(models.Model):
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)

    class Meta:
        verbose_name = "Klientas"
        verbose_name_plural = "Klientai"
        ordering = ['last_name', 'first_name']


class Darbuotojas(models.Model):
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)

    class Meta:
        verbose_name = "Darbuotojas"
        verbose_name_plural = "Darbuotojai"
        ordering = ['last_name', 'first_name']


class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    pastabos = HTMLField("Pastabos", max_length=5000)

    class Meta:
        verbose_name = "Darbas"
        verbose_name_plural = "Darbai"


class Saskaita(models.Model):
    israsymo_data = models.DateTimeField("Išrašymo data")
    suma = models.FloatField("Suma")

    class Meta:
        verbose_name = "Sąskaita"
        verbose_name_plural = "Sąskaitos"
