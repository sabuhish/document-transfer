from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Company(models.Model):
    voen = models.IntegerField(verbose_name="Vöen", unique=True)
    name = models.CharField(max_length=255, verbose_name="sirketin adi")
    ceo_first_name = models.CharField(max_length=120, verbose_name="rehberin adi")
    ceo_lastname =models.CharField(max_length=250)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class AsanImza(models.Model):
    company = models.ForeignKey(Company, verbose_name=(""), on_delete=models.CASCADE)
    asan_imza = models.IntegerField("Asan imza", unique=True)
    asan_nomre  =models.CharField("Asan nomre", unique=True, max_length=20)


class CompanyContacts(models.Model):
    __choices = (
        (1, "Telefon"),
        (2, "email"),
        (3, "address")
    )
    company =models.ForeignKey(Company, on_delete=models.CASCADE)
    contacnt_type = models.IntegerField(choices = __choices)
    comtact = models.CharField(max_length=255, verbose_name="elaqe")