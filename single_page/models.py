from django.db import models

class houses(models.Model):
    housename = models.CharField(max_length=100)
    housepoints = models.IntegerField(max_length=100, null=True)


class boss(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField(max_length=100, null=True)
    maxhp = models.IntegerField(max_length=100, null=True)
    gold = models.CharField(max_length=100)