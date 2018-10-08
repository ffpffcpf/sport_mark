from django.db import models

from sport_mark.model.muscle import Muscle


class Movement(models.Model):
    BODY_PART_CHOICES = (
        ('a', 'ARMS')
    )
    name = models.CharField(max_length=100)
    body_part = models.CharField(max_length=1, choices=BODY_PART_CHOICES)
    muscles = models.ManyToManyField(Muscle)


class TrainingData(models.Model):
    weight = models.IntegerField(max_length=4)
    group_num = models.IntegerField(max_length=2)
    movement = models.ForeignKey('Movement', on_delete=models.CASCADE)




