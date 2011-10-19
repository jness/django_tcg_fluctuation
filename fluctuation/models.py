from django.db import models

class Cards(models.Model):
    class Meta:
        db_table = 'Cards'
        verbose_name = 'Cards'
        verbose_name_plural = 'Cards'

    name = models.CharField(max_length=50)
    rarity = models.CharField(max_length=25)
    mtgset = models.CharField(max_length=75)

class History(models.Model):
    class Meta:
        db_table = 'History'
        verbose_name = 'History'
        verbose_name_plural = 'History'

    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    average = models.CharField(max_length=10)
