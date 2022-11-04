from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
