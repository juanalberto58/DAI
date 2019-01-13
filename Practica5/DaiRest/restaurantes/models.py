from pymongo import MongoClient
from django.db import models


# Create your models here.


client = MongoClient('localhost',27017)

mongo = client['Restaurants']
restaurantes= mongo['RestaurantsCollection']


class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    alergeno = models.CharField(max_length=200)
    precio = models.FloatField(max_length=200)

    def __str__(self):
        return name

class Registro(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dni = models.FloatField(max_length=200, unique=True)

    def __str__(self):
        return name
