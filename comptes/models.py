from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User ,null=True, blank=True, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    living_town = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    domaines = models.CharField(max_length=80)
    genre = models.CharField(max_length=10)

class spirit(models.Model):
    user = models.ForeignKey(User ,null=True, blank=True, on_delete=models.CASCADE)
    young_crue = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    water_baptem = models.CharField(max_length=3)
    spirit_baptem = models.CharField(max_length=3)
    
class scolaire(models.Model):
    user = models.ForeignKey(User ,null=True, blank=True, on_delete=models.CASCADE)
    school_level = models.CharField(max_length=50)
    last_diplom = models.CharField(max_length=50)
    type_bac = models.CharField(max_length=1)
    fields = models.CharField(max_length=200)

class professionnal(models.Model):
    user = models.ForeignKey(User ,null=True, blank=True, on_delete=models.CASCADE)
    working = models.CharField(max_length=3)
    jobs = models.CharField(max_length=80)
    jobs_description = models.TextField(blank=True, default=None)
    cv = models.FileField(upload_to='PDF/CV/', null=True)
    image_de_profil = models.ImageField(upload_to='Pictures/profil', null=True)

    