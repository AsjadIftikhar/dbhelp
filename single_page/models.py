from django.db import models


class Houses(models.Model):
    house_name = models.CharField(max_length=100)
    house_points = models.IntegerField(null=True)


class Boss(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField(null=True)
    max_hp = models.IntegerField(null=True)
    gold = models.CharField(max_length=100)
