from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    Lat = models.FloatField('Широта')
    Lon = models.FloatField('Долгота')
