from django.db import models

class MotherBoard(models.Model):
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
