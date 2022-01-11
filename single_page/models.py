from django.db import models


class houses(models.Model):
    housename = models.CharField(max_length=100)
    housepoints = models.IntegerField(null=True)

    def __str__(self):
        return self.housename


class boss(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField(null=True)
    maxhp = models.IntegerField(null=True)
    gold = models.CharField(max_length=100)

    def __str__(self):
        return self.name
