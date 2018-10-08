from django.db import models
from sport_mark.model.movement import Movement


class Muscle(models.Model):
    movements = models.ManyToManyField(Movement)


class Size(models.Model):
    size = models.FloatField()
    muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE)