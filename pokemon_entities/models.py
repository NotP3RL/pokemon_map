from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Русское название', max_length=200)
    title_en = models.CharField('Английское название', max_length=200, blank=True)
    title_jp = models.CharField('Японское название', max_length=200, blank=True)
    image = models.ImageField('Изображение')
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', related_name='next_evolutions', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', related_name='entities', on_delete=models.CASCADE, null=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появиться', null=True)
    disappeared_at = models.DateTimeField('Исчезнет', null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    attack = models.IntegerField('Атака', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)
