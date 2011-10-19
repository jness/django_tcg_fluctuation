from django.db import models

class Cards(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=25)
    mtgset = models.CharField(max_length=75)

class History(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    average = models.CharField(max_length=10)
