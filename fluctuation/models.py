from django.db import models

class Cards(models.Model):
    class Meta:
        db_table = 'Cards'
        verbose_name = 'Cards'
        verbose_name_plural = 'Cards'

    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=25)
    mtgset = models.CharField(max_length=75)
    average = models.CharField(max_length=10)
    prev_average = models.CharField(max_length=10)
